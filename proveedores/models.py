from django.db import models

class Bodega(models.Model):
    tipo_bodega = models.CharField(max_length=45)
    nombre_responsable = models.CharField(max_length=45)
    
    def __str__(self) -> str:
        return self.tipo_bodega

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Apellido por defecto')
    rut = models.CharField(max_length=12)
    placa_patente = models.CharField(max_length=10)
    empresa = models.CharField(max_length=100)
    numero_contacto = models.CharField(max_length=15)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    retirado = models.BooleanField(default=False)
    bodega = models.ForeignKey(Bodega, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.nombre
    

    
    