from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    placa_patente = models.CharField(max_length=10)
    empresa = models.CharField(max_length=100)
    numero_contacto = models.CharField(max_length=15)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    retirado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nombre
    
class Bodega(models.Model):
    tipo_bodega = models.CharField(max_length=45)
    nombre_responsable = models.CharField(max_length=45)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.tipo_bodega
    
    