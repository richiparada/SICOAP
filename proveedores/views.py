from rest_framework import viewsets
from .models import Proveedor, Bodega
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .decorators import solo_supervisores
from django.utils.timezone import now
from .forms import ProveedorForm, BodegaForm, MonthSelectForm, RegistroForm
from django.contrib.auth.decorators import login_required

@login_required  
def proveedores_list(request):
    proveedores = Proveedor.objects.filter(retirado=False)
    return render(request, 'index.html', {'proveedores': proveedores})

@login_required
def proveedores_info(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'info.html', {'proveedores': proveedores})

@login_required
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

@login_required
def marcar_retiro(request, proveedor_id):
    #Retira a los provedores
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedor.retirado = True
    proveedor.save()
    return redirect('proveedores_list')  # Redirige al listado de proveedores

@solo_supervisores 
@login_required
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

@login_required
@solo_supervisores
def bodega_list(request):
    bodegas = Bodega.objects.all()
    return render(request, 'listabodega.html', {'bodegas': bodegas})

@login_required
@solo_supervisores
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

@login_required
@solo_supervisores
def estadisticas_bodegas(request):
    form = MonthSelectForm(request.GET or None)
    proveedores = Proveedor.objects.all()

    # Filtrar por mes y año
    if form.is_valid():
        month = int(form.cleaned_data['month'])
        year = int(form.cleaned_data['year'])
        proveedores = proveedores.filter(
            fecha_ingreso__year=year,
            fecha_ingreso__month=month
        )

    # Contar las visitas por bodega
    visitas_bodegas = proveedores.values('bodega__tipo_bodega').annotate(visitas=Count('bodega')).order_by('-visitas')

    return render(request, 'estadisticas_bodega.html', {
        'form': form,
        'visitas_bodegas': visitas_bodegas,
    })

@login_required
@solo_supervisores
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro_usuario.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('proveedores_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

