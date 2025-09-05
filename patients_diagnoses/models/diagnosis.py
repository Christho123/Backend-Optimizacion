from django.db import models
from django.utils import timezone

class Diagnosis(models.Model):
    """
    Modelo para gestionar los diagnósticos médicos.
    Basado en la estructura de la tabla diagnoses de la BD.
    """
    
    # Multitenant: cada diagnóstico pertenece a un tenant (Reflexo)
    reflexo = models.ForeignKey(
        'reflexo.Reflexo',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
        verbose_name='Empresa/Tenant'
    )

    code = models.CharField(max_length=255, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de eliminación")
    
    class Meta:
        db_table = 'diagnoses'
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
        ordering = ['code']
        constraints = [
            models.UniqueConstraint(fields=['reflexo', 'code'], name='uniq_diagnosis_per_reflexo_code')
        ]
    
    def soft_delete(self):
        """Soft delete del diagnóstico."""
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])
    
    def restore(self):
        """Restaura un diagnóstico eliminado."""
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])

    def __str__(self):
        return f"{self.code} - {self.name}"