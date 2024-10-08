from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import proveedores_list, proveedores_registro, proveedores_info, marcar_retiro, estadisticas_proveedores, bodega_list, bodega_crear, estadisticas_bodegas, registro, iniciar_sesion, almacen_detail
#from . import views



urlpatterns = [
    path('', iniciar_sesion, name='login'),
    path('index/', proveedores_list, name='proveedores_list'),
    path('registro/', proveedores_registro, name='proveedores_registro'),
    path('info/', proveedores_info, name='proveedores_info'),
    path('retirar/<int:proveedor_id>/', marcar_retiro, name='marcar_retiro'),
    path('estadisticas/', estadisticas_proveedores, name='estadisticas_proveedores'),
    path('bodega/', bodega_crear, name='bodega_crear'),
    path('listabodega/', bodega_list, name='bodega_list'),
    path('estadisticas_bodega/', estadisticas_bodegas, name='estadisticas_bodegas'),
    path('registro_usuarios/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('almacen/<int:almacen_id>/', almacen_detail, name='almacen_detail'),  # Ruta dinámica para almacenes
]