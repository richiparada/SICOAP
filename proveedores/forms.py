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