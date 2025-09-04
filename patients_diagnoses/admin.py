from django.contrib import admin
from .models.patient import Patient
from .models.diagnosis import Diagnosis
from .models.medical_record import MedicalRecord
from architect.utils.tenant import is_global_admin, get_tenant, filter_by_tenant

class CurrentTenantReflexoFilter(admin.SimpleListFilter):
    title = 'reflexo'
    parameter_name = 'reflexo'

    def lookups(self, request, model_admin):
        # Solo mostrar el tenant del usuario actual
        if is_global_admin(request.user):
            from reflexo.models import Reflexo
            return [(r.id, r.name) for r in Reflexo.objects.all().order_by('name')]
        tid = get_tenant(request.user)
        if tid is None:
            return []
        from reflexo.models import Reflexo
        name = Reflexo.objects.filter(id=tid).values_list('name', flat=True).first() or str(tid)
        return [(tid, name)]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(reflexo_id=value)
        # Si no hay valor y el usuario no es global, ya viene filtrado por get_queryset
        return queryset

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname',
        'phone1', 'email', 'reflexo'
    )
    search_fields = (
        'id', 'document_number', 'name', 'paternal_lastname', 'maternal_lastname', 'personal_reference'
    )
    list_filter = (
        'sex', 'region', 'province', 'district', 'document_type', 'created_at', 'deleted_at'
    )
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

    def get_list_filter(self, request):
        base = list(super().get_list_filter(request))
        # Para usuarios de empresa, reemplazar el filtro de reflexo por uno acotado al tenant
        if is_global_admin(request.user):
            return tuple(['reflexo'] + base)
        return tuple([CurrentTenantReflexoFilter] + base)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if is_global_admin(request.user):
            return qs
        return filter_by_tenant(qs, request.user, field='reflexo')

    def get_readonly_fields(self, request, obj=None):
        ro = list(super().get_readonly_fields(request, obj))
        if not is_global_admin(request.user):
            ro.append('reflexo')
        return tuple(ro)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'reflexo' and not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is not None:
                from reflexo.models import Reflexo
                kwargs['queryset'] = Reflexo.objects.filter(id=tenant_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is None:
                from django.core.exceptions import ValidationError
                raise ValidationError("Tu usuario no tiene empresa asignada (reflexo). Comunícate con el administrador.")
            obj.reflexo_id = tenant_id
        super().save_model(request, obj, form, change)

    def changelist_view(self, request, extra_context=None):
        # Si el usuario de empresa no tiene tenant asignado, mostrar advertencia clara
        if not is_global_admin(request.user) and get_tenant(request.user) is None:
            from django.contrib import messages
            messages.warning(
                request,
                "Tu usuario no tiene una empresa asignada (reflexo). No se puede mostrar ningún paciente. Pide al admin que te asigne una empresa."
            )
        return super().changelist_view(request, extra_context)

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created_at')
    search_fields = ('code', 'name')
    ordering = ('code',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnose', 'diagnosis_date', 'status', 'created_at')
    list_filter = ('status', 'diagnosis_date', 'created_at', 'deleted_at')
    search_fields = ('patient__name', 'patient__document_number', 'diagnose__name', 'diagnose__code')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    ordering = ('-diagnosis_date', '-created_at')
    
    fieldsets = (
        ('Información del Paciente', {
            'fields': ('patient',)
        }),
        ('Información del Diagnóstico', {
            'fields': ('diagnose', 'diagnosis_date', 'status')
        }),
        ('Detalles Médicos', {
            'fields': ('symptoms', 'treatment', 'notes')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        })
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related('patient', 'diagnose')
        if is_global_admin(request.user):
            return qs
        # filtra por el tenant del paciente
        return qs.filter(patient__reflexo_id=get_tenant(request.user))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Limita los pacientes a los del tenant
        if db_field.name == 'patient' and not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is not None:
                kwargs['queryset'] = Patient.objects.filter(reflexo_id=tenant_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)