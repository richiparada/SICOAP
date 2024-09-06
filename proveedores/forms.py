from django import forms
from django.contrib.auth.models import User
from .models import Proveedor, Bodega, Perfil
import datetime

#Formulario de registro de proveedores
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'rut', 'empresa', 'placa_patente', 'numero_contacto', 'bodega']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'nombre', 'placeholder': 'Escriba Nombre del proveedor'}),
            'apellido': forms.TextInput(attrs={'class': 'apellido', 'placeholder': 'Escriba Apellido del proveedor'}),
            'rut': forms.TextInput(attrs={'class': 'rut', 'placeholder': 'Escriba Rut del proveedor'}),
            'empresa': forms.TextInput(attrs={'class': 'empresa', 'placeholder': 'Ingrese nombre de la Empresa'}),
            'placa_patente': forms.TextInput(attrs={'class': 'placa_patente', 'placeholder': 'Ingrese Placa Patente del Vehículo'}),
            'numero_contacto': forms.TextInput(attrs={'class': 'numero_contacto', 'placeholder': 'Ingrese número de contacto'}),
            'bodega': forms.Select(attrs={'class': 'form-control'}),
        }
    
    #Normalizar datos
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        return nombre.strip().title() # Eliminar espacios y capitalizar cada palabra
    
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        return apellido.strip().title() # Eliminar espacios y capitalizar cada palabra
    
    def clean_empresa(self):
        empresa = self.cleaned_data.get('empresa')
        return empresa.strip().upper()  # Eliminar espacios y convertir a mayúsculas
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        return rut.replace('.', '').replace('-', '').upper()  # Eliminar puntos, guiones y convertir a mayúsculas

    def clean_placa_patente(self):
        placa_patente = self.cleaned_data.get('placa_patente')
        return placa_patente.replace('-', '').upper()  # Eliminar guiones y convertir a mayúsculas

    def clean_numero_contacto(self):
        numero_contacto = self.cleaned_data.get('numero_contacto')
        return ''.join(filter(str.isdigit, numero_contacto))  # Mantener solo dígitos

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email.strip().lower()  # Eliminar espacios y convertir a minúsculas

#Formulario para registrar Bodega
class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['tipo_bodega', 'nombre_responsable']
        widgets = {
            'tipo_bodega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de bodega'}),
            'nombre_responsable': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del responsable'}),
        }

#Formulario para seleccionar mes        
class MonthSelectForm(forms.Form):
    month = forms.ChoiceField(
        choices=[(i, datetime.date(2008, i, 1).strftime('%B')) for i in range(1, 13)],
        label="Seleccione el Mes",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    year = forms.ChoiceField(
        choices=[(year, year) for year in range(2020, datetime.date.today().year + 1)],
        label="Seleccione el Año",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

#Formulario de Registro de Usuarios
class RegistroForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    rol = forms.ChoiceField(choices=Perfil.ROLES)

    class Meta:
        model = User
        fields = ['username', 'password']

    # Verificar que las contraseñas coincidan
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden. Inténtelo de nuevo.")
        
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
            perfil = Perfil.objects.create(usuario=user, rol=self.cleaned_data['rol'])
        return user