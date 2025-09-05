import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models.payment_type import PaymentType
from architect.utils.tenant import get_tenant

@csrf_exempt
def payment_types_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    tenant_id = get_tenant(request.user)
    qs = PaymentType.objects.filter(deleted_at__isnull=True)
    if tenant_id is not None:
        qs = qs.filter(reflexo_id=tenant_id)
    else:
        qs = qs.none()
    data = [{"id": x.id, "name": x.name} for x in qs]
    return JsonResponse({"payment_types": data})

@csrf_exempt
def payment_type_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    tenant_id = get_tenant(request.user)
    if tenant_id is None:
        return JsonResponse({"error": "Usuario sin empresa asignada"}, status=403)
    pt = PaymentType.objects.create(name=payload.get("name",""), reflexo_id=tenant_id)
    return JsonResponse({"id": pt.id, "name": pt.name}, status=201)

@csrf_exempt
def payment_type_delete(request, pk):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(["DELETE"])
    try:
        tenant_id = get_tenant(request.user)
        base = PaymentType.objects.filter(deleted_at__isnull=True)
        if tenant_id is not None:
            base = base.filter(reflexo_id=tenant_id)
        else:
            base = base.none()
        pt = base.get(pk=pk)
    except PaymentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)
    pt.soft_delete()
    return JsonResponse({"status": "deleted", "id": pk}, status=200)

@csrf_exempt
def payment_type_edit(request, pk):
    if request.method != "PUT":
        return HttpResponseNotAllowed(["PUT"])

    try:
        tenant_id = get_tenant(request.user)
        base = PaymentType.objects.filter(deleted_at__isnull=True)
        if tenant_id is not None:
            base = base.filter(reflexo_id=tenant_id)
        else:
            base = base.none()
        pt = base.get(pk=pk)
    except PaymentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)

    payload = json.loads(request.body.decode() or "{}")

    pt.name = payload.get("name", pt.name)

    pt.save()
    return JsonResponse({
        "id": pt.id,
        "name": pt.name
    }, status=200)