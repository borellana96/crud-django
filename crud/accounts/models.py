from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo_proveedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.IntegerField(null=True, blank=True)
    #tipo = models.CharField(max_length=20, null=True, blank=True)