# -*- coding: utf-8 -*-
"""
Vistas para la aplicación de terapeutas.
Maneja las operaciones CRUD y renderizado de templates.
"""

from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from therapists.models.therapist import Therapist
from therapists.serializers.therapist import TherapistSerializer
from architect.utils.tenant import filter_by_tenant, is_global_admin


class TherapistViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de terapeutas.
    Incluye:
      - Filtros por estado y por región/provincia/distrito (IDs).
      - Búsqueda por campos.
      - Soft delete y restauración.
    """
    serializer_class = TherapistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
        "last_name_paternal",
        "last_name_maternal",
        "document_number",
        "document_type",
        "email",
        "phone",
        "address",
        # búsqueda por nombres de ubicaciones (FK)
        "region__name",
        "province__name",
        "district__name",
    ]

    def get_queryset(self):
        """
        - Usa select_related para evitar N+1 en las FKs de ubicación.
        - Filtra por activo/inactivo (param 'active').
        - Filtra opcionalmente por IDs de region/province/district.
        """
        qs = (
            Therapist.objects.select_related("region", "province", "district")
            .all()
        )
        # Tenant isolation
        qs = filter_by_tenant(qs, self.request.user, field='reflexo')

        # filtro por estado (activo por defecto)
        active = self.request.query_params.get("active", "true").lower()
        if active in ("true", "1", "yes"):
            qs = qs.filter(deleted_at__isnull=True)
        elif active in ("false", "0", "no"):
            qs = qs.filter(deleted_at__isnull=False)

        # filtros por ubicación (IDs)
        region = self.request.query_params.get("region")
        province = self.request.query_params.get("province")
        district = self.request.query_params.get("district")
        if region:
            qs = qs.filter(region_id=region)
        if province:
            qs = qs.filter(province_id=province)
        if district:
            qs = qs.filter(district_id=district)

        return qs

    def perform_create(self, serializer):
        # Asigna tenant automáticamente si no es admin global
        if not is_global_admin(self.request.user):
            serializer.save(reflexo_id=getattr(self.request.user, 'reflexo_id', None))
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Evita cambiar el tenant para usuarios no admin
        if not is_global_admin(self.request.user):
            serializer.save(reflexo_id=getattr(self.request.user, 'reflexo_id', None))
        else:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        """
        Soft delete - marca como inactivo en lugar de eliminar.
        """
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def inactive(self, request):
        """
        Endpoint para obtener terapeutas inactivos.
        Respeta paginación y serializer.
        """
        queryset = self.get_queryset().filter(deleted_at__isnull=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(self.get_serializer(queryset, many=True).data)

    @action(detail=True, methods=["post", "patch"])
    def restore(self, request, pk=None):
        """
        Restaura un terapeuta marcándolo como activo.
        """
        try:
            therapist = Therapist.objects.get(pk=pk, deleted_at__isnull=False)
        except Therapist.DoesNotExist:
            return Response({"detail": "No encontrado."}, status=status.HTTP_404_NOT_FOUND)
        therapist.restore()
        return Response(self.get_serializer(therapist).data)


def index(request):
    """
    Vista para renderizar la página principal de terapeutas.
    """
    return render(request, "therapists_ui.html")
