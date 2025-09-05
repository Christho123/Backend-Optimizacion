import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models.history import History
from ..models.document_type import DocumentType
from architect.utils.tenant import filter_by_tenant, get_tenant
from patients_diagnoses.models.patient import Patient

@csrf_exempt
def histories_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    
    # Forzar aislamiento por tenant aunque sea admin global
    tenant_id = get_tenant(request.user)
    qs = History.objects.filter(deleted_at__isnull=True).select_related("patient")
    if tenant_id is not None:
        qs = qs.filter(reflexo_id=tenant_id)
    else:
        qs = qs.none()

    data = [{
        "id": h.id,
        "patient": h.patient_id,
        "patient_name": f"{h.patient.name} {h.patient.paternal_lastname}" if h.patient else None
    } for h in qs]
    return JsonResponse({"histories": data})

@csrf_exempt
def history_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    patient_id = payload.get("patient")
    tenant_id = get_tenant(request.user)

    # Validar campos obligatorios
    if patient_id is None:
        return JsonResponse({"error": "Campos obligatorios faltantes"}, status=400)

    # Verificar si ya existe un historial activo para este paciente
    # Validar que el paciente pertenezca al mismo tenant
    try:
        patient = filter_by_tenant(Patient.objects.all(), request.user, field='reflexo').get(pk=patient_id)
    except Patient.DoesNotExist:
        return JsonResponse({"error": "Paciente no encontrado para tu empresa"}, status=404)

    existing_history = filter_by_tenant(
        History.objects.filter(deleted_at__isnull=True),
        request.user,
        field='reflexo'
    ).filter(patient_id=patient_id).first()
    
    if existing_history:
        return JsonResponse({
            "error": "Ya existe un historial activo para este paciente",
            "existing_history_id": existing_history.id
        }, status=409)
    
    try:
        h = History.objects.create(patient_id=patient_id, reflexo_id=tenant_id)
        return JsonResponse({"id": h.id}, status=201)
    except Exception as e:
        return JsonResponse({"error": "Error al crear el historial"}, status=500)

@csrf_exempt
def history_update(request, pk):
    """Actualizar historial (PUT/PATCH)"""
    if request.method not in ["PUT", "PATCH"]:
        return HttpResponseNotAllowed(["PUT", "PATCH"])
    
    try:
        h = History.objects.filter(deleted_at__isnull=True).get(pk=pk)
    except History.DoesNotExist:
        return JsonResponse({"error": "No encontrado"}, status=404)
    
    # Manejo de JSON inválido
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    # Actualizar campos permitidos
    allowed_fields = ['testimony', 'private_observation', 'observation', 'height', 'weight', 'last_weight', 'menstruation', 'diu_type', 'gestation']
    
    for field in allowed_fields:
        if field in payload:
            setattr(h, field, payload[field])
    
    try:
        h.save()
        return JsonResponse({
            "status": "updated",
            "id": h.id,
            "data": {
                "testimony": h.testimony,
                "observation": h.observation,
                "height": float(h.height) if h.height else None,
                "weight": float(h.weight) if h.weight else None,
            }
        })
    except Exception as e:
        return JsonResponse({"error": "Error al actualizar el historial"}, status=500)

@csrf_exempt
def history_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    try:
        tenant_id = get_tenant(request.user)
        base = History.objects.filter(deleted_at__isnull=True)
        if tenant_id is not None:
            base = base.filter(reflexo_id=tenant_id)
        else:
            base = base.none()
        h = base.get(pk=pk)
    except History.DoesNotExist:
        return JsonResponse({"error":"No encontrado"}, status=404)
    
    h.soft_delete()  # Debe marcar deleted_at = timezone.now()
    return JsonResponse({"status": "deleted"})