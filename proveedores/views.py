from rest_framework import viewsets
from .models import Proveedor, Bodega
from .serializers import ProveedorSerializer, BodegaSerializer
from django.shortcuts import render

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'index.html', {'proveedores': proveedores})

def proveedores_registro(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'registro.html', {'proveedores': proveedores})