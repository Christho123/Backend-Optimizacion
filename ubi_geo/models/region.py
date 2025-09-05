from django.db import models

class Region(models.Model):
    """
    Modelo para gestionar las regiones.
    Basado en la estructura de la tabla regions de la BD.
    """
    
    # Multitenant: cada región pertenece a un tenant (Reflexo)
    reflexo = models.ForeignKey(
        'reflexo.Reflexo',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
        verbose_name='Empresa/Tenant'
    )

    name = models.CharField(max_length=255, verbose_name="Nombre")
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de eliminación")

    class Meta:
        db_table = 'regions'
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=['reflexo', 'name'], name='uniq_region_per_reflexo_name')
        ]

    def __str__(self):
        return self.name
