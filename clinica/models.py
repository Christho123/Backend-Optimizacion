from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Reflexo = models.ForeignKey('reflexo.Reflexo', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.username} ({self.Reflexo})" if self.Reflexo else self.username