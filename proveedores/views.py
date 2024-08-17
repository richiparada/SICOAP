from rest_framework import viewsets
from .models import Proveedor, Bodega
from .serializers import ProveedorSerializer, BodegaSerializer
from django.shortcuts import render, redirect
from .forms import ProveedorForm

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'index.html', {'proveedores': proveedores})

'''def proveedores_registro(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'registro.html', {'proveedores': proveedores})'''

def proveedores_info(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'info.html', {'proveedores': proveedores})

def proveedores_registro(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('proveedores_list')  # Redirige a la lista de proveedores después de guardar   

    else:
        form = ProveedorForm()
    
    return render(request, 'registro.html', {'form': form})