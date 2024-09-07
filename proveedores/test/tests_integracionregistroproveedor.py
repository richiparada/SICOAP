import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from proveedores.models import Perfil
from django.conf import settings

@pytest.mark.django_db
def test_registro_usuario():
    client = Client()
    
    # Define datos para el formulario
    data = {
        'username': 'nuevo_usuario',
        'password': 'ContraseñaSegura123',
        'password2': 'ContraseñaSegura123',
        'rol': 'supervisor'  # Ajusta según las opciones definidas en Perfil.ROLES
    }

    # Accede a la página de registro (GET request)
    response = client.get(reverse('registro'))
    assert response.status_code == 200
    assert 'form' in response.context

    # Envía los datos del formulario (POST request)
    response = client.post(reverse('registro'), data=data)
    
    # Verifica que el redireccionamiento ocurrió correctamente
    assert response.status_code == 302
    assert response.url == reverse('login')

    # Verifica que el usuario fue creado
    assert User.objects.filter(username='nuevo_usuario').exists()
    
    # Verifica que el perfil fue creado
    user = User.objects.get(username='nuevo_usuario')
    perfil = Perfil.objects.get(usuario=user)
    assert perfil.rol == 'supervisor'

    # Verifica que las contraseñas se han guardado correctamente (hashed)
    assert user.check_password('ContraseñaSegura123')
