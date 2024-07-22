from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, BodegaViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'bodegas', BodegaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]