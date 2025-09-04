from django.contrib import admin
from .models.appointment import Appointment
from .models.appointment_status import AppointmentStatus
from .models.ticket import Ticket
from architect.utils.tenant import is_global_admin, get_tenant, filter_by_tenant


@admin.register(AppointmentStatus)
class AppointmentStatusAdmin(admin.ModelAdmin):
    """
    Configuración del admin para AppointmentStatus.
    """
    list_display = ['name', 'description', 'appointments_count', 'created_at']
    list_filter = ['created_at', 'updated_at', 'deleted_at']
    search_fields = ['name', 'description']
    readonly_fields = ['appointments_count', 'created_at', 'updated_at', 'deleted_at']
    ordering = ['name']

    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description')
        }),
        ('Información del Sistema', {
            'fields': ('appointments_count', 'created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        }),
    )


# --- Inline opcional para crear/ver Tickets desde la Cita ---
class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 0
    autocomplete_fields = ['appointment']  # no carga listas enormes
    readonly_fields = ['is_paid', 'is_pending', 'payment_date', 'created_at', 'updated_at', 'deleted_at']
    fieldsets = (
        ('Información del Ticket', {
            'fields': ('ticket_number', 'amount', 'payment_method', 'description')
        }),
        ('Estado del Pago', {
            'fields': ('status',)
        }),
        ('Relaciones', {
            'fields': ('appointment',),
            'description': 'La cita se completa automáticamente al usar el inline.'
        }),
        ('Información del Sistema', {
            'fields': ('is_paid', 'is_pending', 'payment_date', 'created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'appointment_date', 'hour', 'appointment_status',
        'room', 'is_completed', 'deleted_at'
    ]
    list_filter = [
        'appointment_date', 'appointment_status', 'room',
        'created_at', 'deleted_at'
    ]
    search_fields = ['ailments', 'diagnosis', 'observation', 'ticket_number']
    readonly_fields = ['is_completed', 'is_pending', 'created_at', 'updated_at', 'deleted_at']
    ordering = ['-appointment_date', '-hour']

    # 👇 según prefieras
    raw_id_fields = ['patient', 'therapist', 'history']
    # o bien
    autocomplete_fields = ['payment_status']

    fieldsets = (
        ('Información de la Cita', {
            'fields': ('appointment_date', 'hour', 'room')
        }),
        ('Información Médica', {
            'fields': ('ailments', 'diagnosis', 'surgeries', 'reflexology_diagnostics', 'medications', 'observation')
        }),
        ('Fechas de Tratamiento', {
            'fields': ('initial_date', 'final_date')
        }),
        ('Información de Pago', {
            'fields': ('social_benefit', 'payment_detail', 'payment', 'ticket_number')
        }),
        ('Relaciones', {
            'fields': ('patient', 'therapist', 'history', 'payment_status', 'appointment_status'),
            'description': 'Selecciona paciente, terapeuta, historial y estado de pago.'
        }),
        ('Información del Sistema', {
            'fields': ('is_completed', 'is_pending', 'created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        qs = (super()
              .get_queryset(request)
              .select_related('patient', 'therapist', 'history', 'payment_status'))
        if is_global_admin(request.user):
            return qs
        return filter_by_tenant(qs, request.user, field='reflexo')

    def get_readonly_fields(self, request, obj=None):
        ro = list(super().get_readonly_fields(request, obj))
        if not is_global_admin(request.user):
            ro.append('reflexo')
        return tuple(ro)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is not None:
                if db_field.name == 'patient':
                    from patients_diagnoses.models import Patient
                    kwargs['queryset'] = Patient.objects.filter(reflexo_id=tenant_id)
                elif db_field.name == 'therapist':
                    from therapists.models import Therapist
                    kwargs['queryset'] = Therapist.objects.filter(reflexo_id=tenant_id)
                elif db_field.name == 'history':
                    from histories_configurations.models import History
                    kwargs['queryset'] = History.objects.filter(reflexo_id=tenant_id)
                elif db_field.name == 'reflexo':
                    from reflexo.models import Reflexo
                    kwargs['queryset'] = Reflexo.objects.filter(id=tenant_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not is_global_admin(request.user):
            obj.reflexo_id = get_tenant(request.user)
        super().save_model(request, obj, form, change)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Configuración del admin para Ticket.
    """
    list_display = [
        'ticket_number', 'amount', 'payment_method', 'status',
        'is_paid', 'payment_date', 'deleted_at'
    ]
    list_filter = [
        'payment_method', 'status', 'payment_date', 'created_at', 'deleted_at'
    ]
    search_fields = ['ticket_number', 'description']
    readonly_fields = ['is_paid', 'is_pending', 'payment_date', 'created_at', 'updated_at', 'deleted_at']
    ordering = ['-payment_date']

    # ✅ Para no cargar todas las citas en un <select>
    autocomplete_fields = ['appointment']  # (usa raw_id_fields = ['appointment'] si prefieres)

    fieldsets = (
        ('Información del Ticket', {
            'fields': ('ticket_number', 'amount', 'payment_method', 'description')
        }),
        ('Estado del Pago', {
            'fields': ('status',)
        }),
        ('Relaciones', {
            # ✅ Campo necesario para evitar el NOT NULL
            'fields': ('appointment',),
            'description': 'Selecciona la cita a la que pertenece este ticket'
        }),
        ('Información del Sistema', {
            'fields': ('is_paid', 'is_pending', 'payment_date', 'created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_paid', 'mark_as_cancelled']

    def mark_as_paid(self, request, queryset):
        """Acción para marcar tickets como pagados"""
        updated = queryset.update(status='paid')
        self.message_user(request, f'{updated} tickets marcados como pagados.')
    mark_as_paid.short_description = "Marcar como pagado"

    def mark_as_cancelled(self, request, queryset):
        """Acción para marcar tickets como cancelados"""
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} tickets marcados como cancelados.')
    mark_as_cancelled.short_description = "Marcar como cancelado"

    def get_queryset(self, request):
        """Optimiza las consultas con select_related y aplica tenant"""
        qs = super().get_queryset(request).select_related('appointment')
        if is_global_admin(request.user):
            return qs
        tenant_id = get_tenant(request.user)
        return qs.filter(appointment__reflexo_id=tenant_id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'appointment' and not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is not None:
                kwargs['queryset'] = Appointment.objects.filter(reflexo_id=tenant_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_changeform_initial_data(self, request):
        """
        Permite precargar la cita si vienes con ?appointment=<id> en la URL de alta:
        /admin/appointments_status/ticket/add/?appointment=123
        """
        initial = super().get_changeform_initial_data(request)
        aid = request.GET.get("appointment")
        if aid:
            initial["appointment"] = aid
        return initial
