import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from ..models.history import History
from ..models.document_type import DocumentType

@csrf_exempt
def histories_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    
    qs = History.objects.filter(deleted_at__isnull=True).select_related("patient")
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
    
    # Manejo de JSON inválido
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    patient_id = payload.get("patient")

    # Validar campos obligatorios
    if patient_id is None:
        return JsonResponse({"error": "Campos obligatorios faltantes"}, status=400)

    # Verificar si ya existe un historial activo para este paciente
    existing_history = History.objects.filter(
        patient_id=patient_id,
        deleted_at__isnull=True
    ).first()
    
    if existing_history:
        return JsonResponse({
            "error": "Ya existe un historial activo para este paciente",
            "existing_history_id": existing_history.id
        }, status=409)
    
    try:
        h = History.objects.create(patient_id=patient_id)
        return JsonResponse({"id": h.id}, status=201)
    except Exception as e:
        return JsonResponse({"error": "Error al crear el historial"}, status=500)

@csrf_exempt
def history_update(request, pk):
    """
    Endpoint PUT para actualizar un historial médico existente
    """
    if request.method != "PUT":
        return HttpResponseNotAllowed(["PUT"])
    
    try:
        # Buscar el historial activo
        history = History.objects.filter(deleted_at__isnull=True).get(pk=pk)
    except History.DoesNotExist:
        return JsonResponse({"error": "Historial no encontrado o eliminado"}, status=404)
    
    # Manejo de JSON inválido
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    
    # Campos permitidos para actualización
    allowed_fields = {
        'testimony': 'testimony',
        'private_observation': 'private_observation',
        'observation': 'observation',
        'height': 'height',
        'weight': 'weight',
        'last_weight': 'last_weight',
        'menstruation': 'menstruation',
        'diu_type': 'diu_type',
        'gestation': 'gestation',
        'patient': 'patient_id'  # Si se permite cambiar el paciente
    }
    
    # Validar que el paciente no tenga otro historial activo (si se cambia el paciente)
    new_patient_id = payload.get('patient')
    if new_patient_id and new_patient_id != history.patient_id:
        existing_history = History.objects.filter(
            patient_id=new_patient_id,
            deleted_at__isnull=True
        ).exclude(pk=pk).first()
        
        if existing_history:
            return JsonResponse({
                "error": "Ya existe un historial activo para el nuevo paciente",
                "existing_history_id": existing_history.id
            }, status=409)
    
    try:
        with transaction.atomic():
            # Actualizar campos permitidos
            for field_name, model_field in allowed_fields.items():
                if field_name in payload:
                    value = payload[field_name]
                    
                    # Convertir valores booleanos si es necesario
                    if field_name in ['testimony', 'menstruation', 'gestation']:
                        if isinstance(value, str):
                            value = value.lower() in ('true', '1', 'yes', 'si')
                    
                    # Para campos decimales, manejar valores vacíos
                    if field_name in ['height', 'weight', 'last_weight']:
                        if value == '' or value is None:
                            setattr(history, model_field, None)
                        else:
                            setattr(history, model_field, value)
                    else:
                        setattr(history, model_field, value)
            
            # Guardar los cambios
            history.save()
            
            # Preparar respuesta con datos actualizados
            updated_data = {
                "id": history.id,
                "patient": history.patient_id,
                "testimony": history.testimony,
                "private_observation": history.private_observation,
                "observation": history.observation,
                "height": float(history.height) if history.height else None,
                "weight": float(history.weight) if history.weight else None,
                "last_weight": float(history.last_weight) if history.last_weight else None,
                "menstruation": history.menstruation,
                "diu_type": history.diu_type,
                "gestation": history.gestation,
                "updated_at": history.updated_at.isoformat() if history.updated_at else None
            }
            
            return JsonResponse({
                "message": "Historial actualizado exitosamente",
                "history": updated_data
            }, status=200)
            
    except Exception as e:
        return JsonResponse({"error": f"Error al actualizar el historial: {str(e)}"}, status=500)

@csrf_exempt
def history_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    try:
        h = History.objects.filter(deleted_at__isnull=True).get(pk=pk)
    except History.DoesNotExist:
        return JsonResponse({"error":"No encontrado"}, status=404)
    
    h.soft_delete()  # Debe marcar deleted_at = timezone.now()
    return JsonResponse({"status": "deleted"})