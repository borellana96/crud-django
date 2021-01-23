from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    marca = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre  # Para que se vea en Admin el nombre del objeto
