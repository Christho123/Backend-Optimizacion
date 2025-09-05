import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models.payment_type import PaymentType

@csrf_exempt
def payment_types_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    qs = PaymentType.objects.filter(deleted_at__isnull=True)
    data = [{"id": x.id, "name": x.name} for x in qs]
    return JsonResponse({"payment_types": data})

@csrf_exempt
def payment_type_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    pt = PaymentType.objects.create(name=payload.get("name",""))
    return JsonResponse({"id": pt.id, "name": pt.name}, status=201)

@csrf_exempt
def payment_type_delete(request, pk):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(["DELETE"])
    try:
        pt = PaymentType.objects.get(pk=pk, deleted_at__isnull=True)
    except PaymentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)
    pt.soft_delete()
    return JsonResponse({"status": "deleted", "id": pk}, status=200)

@csrf_exempt
def payment_type_edit(request, pk):
    if request.method not in ["PUT", "PATCH"]:
        return HttpResponseNotAllowed(["PUT", "PATCH"])

    try:
        pt = PaymentType.objects.get(pk=pk, deleted_at__isnull=True)
    except PaymentType.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)

    payload = json.loads(request.body.decode() or "{}")
    
    # Para PUT, actualizar todos los campos; para PATCH, solo los proporcionados
    if request.method == "PUT":
        pt.name = payload.get("name", pt.name)
    else:  # PATCH
        if "name" in payload:
            pt.name = payload["name"]

    pt.save()
    return JsonResponse({
        "id": pt.id,
        "name": pt.name
    }, status=200)