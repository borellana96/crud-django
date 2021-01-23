from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.register(Product)
admin.site.site_header = 'Administración de Proveedores'