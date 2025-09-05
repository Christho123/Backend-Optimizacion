from django.contrib import admin
from .models.payment_type import PaymentType
from .models.document_type import DocumentType
from .models.history import History
from .models.predetermined_price import PredeterminedPrice
from .models import PaymentStatus
from architect.utils.tenant import is_global_admin, get_tenant, filter_by_tenant

#Registrar el modelo en el admin
@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'testimony', 'height', 'weight', 'reflexo', 'created_at')
    list_filter = ('testimony', 'reflexo', 'created_at', 'deleted_at')
    search_fields = ('patient__name', 'patient__document_number')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

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
        if not is_global_admin(request.user):
            tenant_id = get_tenant(request.user)
            if tenant_id is not None:
                if db_field.name == 'patient':
                    from patients_diagnoses.models import Patient
                    kwargs['queryset'] = Patient.objects.filter(reflexo_id=tenant_id)
                elif db_field.name == 'reflexo':
                    from reflexo.models import Reflexo
                    kwargs['queryset'] = Reflexo.objects.filter(id=tenant_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not is_global_admin(request.user):
            obj.reflexo_id = get_tenant(request.user)
        super().save_model(request, obj, form, change)

@admin.register(PredeterminedPrice)
class PredeterminedPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']  # necesario para el autocompletado
    list_display = ['name', 'description']
