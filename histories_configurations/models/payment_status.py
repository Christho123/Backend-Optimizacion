# histories_configurations/models/payment_status.py
from django.db import models

class PaymentStatus(models.Model):
    id = models.AutoField(primary_key=True)
    # Multitenant: cada estado de pago pertenece a un tenant (Reflexo)
    reflexo = models.ForeignKey(
        'reflexo.Reflexo',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
        verbose_name='Empresa/Tenant'
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'payment_status'   # nombre de tabla esperado
        managed = True                # permitir que Django cree la tabla
        verbose_name = "Estado de pago"
        verbose_name_plural = "Estados de pago"
        constraints = [
            models.UniqueConstraint(fields=['reflexo', 'name'], name='uniq_payment_status_per_reflexo_name')
        ]

    def __str__(self):
        return self.name
