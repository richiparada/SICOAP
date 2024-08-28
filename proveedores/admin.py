from django.contrib import admin
from .models import Proveedor, Bodega

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'placa_patente', 'empresa', 'numero_contacto')
    search_fields = ('nombre', 'apellido', 'rut', 'empresa', 'placa_patente')

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('tipo_bodega', 'nombre_responsable', 'proveedor')
    search_fields = ('tipo_bodega', 'nombre_responsable', 'proveedor__nombre')
    list_filter = ('proveedor',)