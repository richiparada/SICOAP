from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, BodegaViewSet, proveedores_list, proveedores_registro, proveedores_info, marcar_retiro, estadisticas_proveedores, bodega_crear

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'bodegas', BodegaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', proveedores_list, name='proveedores_list'),
    path('registro/', proveedores_registro, name='proveedores_registro'),
    path('info/', proveedores_info, name='proveedores_info'),
    path('retirar/<int:proveedor_id>/', marcar_retiro, name='marcar_retiro'),
    path('estadisticas/', estadisticas_proveedores, name='estadisticas_proveedores'),
    path('bodega/', bodega_crear, name='bodega_crear'),
]