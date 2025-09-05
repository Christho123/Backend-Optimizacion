from django.db import models
from .region import Region

class Province(models.Model):
    """
    Modelo para gestionar las provincias.
    Basado en la estructura de la tabla provinces de la BD.
    """
    
    # Multitenant: cada provincia pertenece a un tenant (Reflexo)
    reflexo = models.ForeignKey(
        'reflexo.Reflexo',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
        verbose_name='Empresa/Tenant'
    )

    name = models.CharField(max_length=255, verbose_name="Nombre")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región")
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de eliminación")

    class Meta:
        db_table = 'provinces'
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=['reflexo', 'name'], name='uniq_province_per_reflexo_name')
        ]

    def __str__(self):
        return f"{self.name} ({self.region.name})"
