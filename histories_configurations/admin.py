from django.contrib import admin
from .models.payment_type import PaymentType
from .models.document_type import DocumentType
from .models.history import History
from .models.predetermined_price import PredeterminedPrice
from .models import PaymentStatus
from architect.utils.tenant import filter_by_tenant, get_tenant, is_global_admin

class BaseTenantAdmin(admin.ModelAdmin):
    """Admin base para aislar por tenant (reflexo)."""
    tenant_field_name = 'reflexo'
    # No readonly fields by default; we'll add dynamically if they exist on the model

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if is_global_admin(request.user):
            return qs
        return filter_by_tenant(qs, request.user, field=self.tenant_field_name)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filtrar FKs por tenant para evitar ver entidades de otros tenants
        from django.db.models import ForeignKey
        field_name = db_field.name
        if isinstance(db_field, ForeignKey):
            if is_global_admin(request.user):
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            # Filtrar el propio campo tenant si es FK
            if field_name == self.tenant_field_name:
                tenant_id = get_tenant(request.user)
                if tenant_id is not None:
                    kwargs['queryset'] = db_field.remote_field.model.objects.filter(pk=tenant_id)
            else:
                # Para otros FKs, intentar filtrar por el mismo campo tenant si existe
                rel_model = db_field.remote_field.model
                if hasattr(rel_model, self.tenant_field_name):
                    kwargs['queryset'] = filter_by_tenant(rel_model.objects.all(), request.user, field=self.tenant_field_name)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        ro = list(super().get_readonly_fields(request, obj))
        # El campo tenant solo es de solo lectura para usuarios no admin
        if not is_global_admin(request.user) and self.tenant_field_name not in ro:
            ro.append(self.tenant_field_name)
        # Agregar timestamps solamente si existen en el modelo
        try:
            model_fields = {f.name for f in self.model._meta.get_fields()}
        except Exception:
            model_fields = set()
        for fname in ('created_at', 'updated_at', 'deleted_at'):
            if fname in model_fields and fname not in ro:
                ro.append(fname)
        return tuple(ro)

    def save_model(self, request, obj, form, change):
        # Asignar tenant automáticamente solo para no-admins o si no viene seteado
        tenant_id = get_tenant(request.user)
        if not is_global_admin(request.user):
            if tenant_id is not None:
                setattr(obj, f"{self.tenant_field_name}_id", tenant_id)
        else:
            # Si es admin y no escogió tenant, usar el suyo si existe
            if getattr(obj, f"{self.tenant_field_name}_id", None) is None and tenant_id is not None:
                setattr(obj, f"{self.tenant_field_name}_id", tenant_id)
        super().save_model(request, obj, form, change)

#Registrar el modelo en el admin
@admin.register(PaymentType)
class PaymentTypeAdmin(BaseTenantAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(DocumentType)
class DocumentTypeAdmin(BaseTenantAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(History)
class HistoryAdmin(BaseTenantAdmin):
    list_display = ('id', 'patient', 'testimony', 'height', 'weight', 'created_at')
    list_filter = ('testimony', 'created_at', 'deleted_at')
    search_fields = ('patient__name', 'patient__document_number')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Prefijar el valor de reflexo solo para usuarios no admin
        if not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if 'reflexo' in form.base_fields and tenant_id is not None:
                form.base_fields['reflexo'].initial = tenant_id
        return form

@admin.register(PredeterminedPrice)
class PredeterminedPriceAdmin(BaseTenantAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(PaymentStatus)
class PaymentStatusAdmin(BaseTenantAdmin):
    search_fields = ['name', 'description']  # necesario para el autocompletado
    list_display = ['name', 'description']
