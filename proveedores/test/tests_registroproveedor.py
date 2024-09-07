import pytest
from proveedores.models import Proveedor, Bodega
from django.utils import timezone

@pytest.mark.django_db
def test_proveedores_registro():
    # Crear una bodega para asignar al proveedor
    bodega = Bodega.objects.create(tipo_bodega="Almacen General", nombre_responsable="Juan Pérez")

    # Crear un proveedor
    proveedor = Proveedor.objects.create(
        nombre="Pedro",
        apellido="Sánchez",
        rut="123456789",
        placa_patente="ABC1234",
        empresa="Empresa X",
        numero_contacto="987654321",
        fecha_ingreso=timezone.now(),
        retirado=False,
        bodega=bodega
    )

    # Comprobar que el proveedor fue creado correctamente
    assert proveedor.nombre == "Pedro"
    assert proveedor.apellido == "Sánchez"
    assert proveedor.rut == "123456789"
    assert proveedor.empresa == "Empresa X"
    assert proveedor.bodega.tipo_bodega == "Almacen General"