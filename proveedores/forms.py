from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'rut', 'empresa', 'placa_patente', 'numero_contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'nombre', 'placeholder': 'Escriba Nombre del proveedor'}),
            'apellido': forms.TextInput(attrs={'class': 'apellido', 'placeholder': 'Escriba Apellido del proveedor'}),
            'rut': forms.TextInput(attrs={'class': 'rut', 'placeholder': 'Escriba Rut del proveedor'}),
            'empresa': forms.TextInput(attrs={'class': 'empresa', 'placeholder': 'Ingrese nombre de la Empresa'}),
            'placa_patente': forms.TextInput(attrs={'class': 'placa_patente', 'placeholder': 'Ingrese Placa Patente del Vehículo'}),
            'numero_contacto': forms.TextInput(attrs={'class': 'numero_contacto', 'placeholder': 'Ingrese número de contacto'}),
        }
    
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