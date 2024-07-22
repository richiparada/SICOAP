from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    placa_patente = models.CharField(max_length=10)
    empresa = models.CharField(max_length=100)
    numero_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre