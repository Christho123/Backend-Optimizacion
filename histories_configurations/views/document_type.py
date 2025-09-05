import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models.document_type import DocumentType
from architect.utils.tenant import get_tenant

@csrf_exempt
def document_types_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    tenant_id = get_tenant(request.user)
    qs = DocumentType.objects.filter(deleted_at__isnull=True)
    if tenant_id is not None:
        qs = qs.filter(reflexo_id=tenant_id)
    else:
        qs = qs.none()
    data = [{"id": x.id, "name": x.name} for x in qs]
    return JsonResponse({"document_types": data})

@csrf_exempt
def document_type_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    tenant_id = get_tenant(request.user)
    if tenant_id is None:
        return JsonResponse({"error": "Usuario sin empresa asignada"}, status=403)
    dt = DocumentType.objects.create(name=payload.get("name", ""), reflexo_id=tenant_id)
    return JsonResponse({"id": dt.id, "name": dt.name}, status=201)


@csrf_exempt
def document_type_delete(request, pk):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(["DELETE"])
    try:
        tenant_id = get_tenant(request.user)
        base = DocumentType.objects.filter(deleted_at__isnull=True)
        if tenant_id is not None:
            base = base.filter(reflexo_id=tenant_id)
        else:
            base = base.none()
        dt = base.get(pk=pk)
    except DocumentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)
    dt.soft_delete()
    return JsonResponse({"status": "deleted", "id": pk}, status=200)

@csrf_exempt
def document_type_edit(request, pk):
    if request.method != "PUT":
        return HttpResponseNotAllowed(["PUT"])

    try:
        dt = DocumentType.objects.get(pk=pk, deleted_at__isnull=True)
    except DocumentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)
    payload = json.loads(request.body.decode() or "{}")
    dt.name = payload.get("name", dt.name)

    dt.save()
    return JsonResponse({
        "id": dt.id,
        "name": dt.name
    }, status=200)
