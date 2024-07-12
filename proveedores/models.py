from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    numero_contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre