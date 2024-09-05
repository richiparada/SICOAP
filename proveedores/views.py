from rest_framework import viewsets
from .models import Proveedor, Bodega
from .serializers import ProveedorSerializer, BodegaSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.db.models.functions import TruncMonth
from .forms import ProveedorForm, BodegaForm

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    
def proveedores_list(request):
    proveedores = Proveedor.objects.filter(retirado=False)
    return render(request, 'index.html', {'proveedores': proveedores})

def proveedores_info(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'info.html', {'proveedores': proveedores})

def proveedores_registro(request):
    #Registra a los proveedores
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            bodega_id = request.POST.get('bodega')
            if bodega_id:
                proveedor.bodega = Bodega.objects.get(id=bodega_id)
            print(proveedor.nombre, proveedor.apellido, proveedor.rut, proveedor.empresa, proveedor.placa_patente, proveedor.numero_contacto)
            proveedor.save()
            return redirect('proveedores_list')  # Redirige a la lista de proveedores después de guardar   
        else:
            print(form.errors)
    else:
        form = ProveedorForm()
    bodegas = Bodega.objects.all()
    return render(request, 'registro.html', {'form': form, 'bodegas': bodegas})

def marcar_retiro(request, proveedor_id):
    #Retira a los provedores
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedor.retirado = True
    proveedor.save()
    return redirect('proveedores_list')  # Redirige al listado de proveedores

def estadisticas_proveedores(request):
    # Contar la cantidad de proveedores registrados por mes
    proveedores_por_mes = (
        Proveedor.objects.annotate(month=TruncMonth('fecha_ingreso'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    
    # Pasar los datos a la plantilla
    context = {
        'proveedores_por_mes': proveedores_por_mes,
    }
    return render(request, 'estadisticas.html', context)

def bodega_list(request):
    bodegas = Bodega.objects.all()
    return render(request, 'listabodega.html', {'bodegas': bodegas})

def bodega_crear(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bodega_list')
        else:
            print(form.errors)
    else:
        form = BodegaForm()
    return render(request, 'bodega.html', {'form': form})


def bodega_modificar(request, bodega_id):
    bodega = get_object_or_404(Bodega, id=bodega_id)
    if request.method == 'POST':
        form = BodegaForm(request.POST, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect('bodega_list')
    else:
        form = BodegaForm(instance=bodega)
    return render(request, 'modificarbodega.html', {'form': form})