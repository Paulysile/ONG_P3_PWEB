from django import forms
from django.forms import ModelForm
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedores
        fields= ['rut','razonsocial','descripcion','telefono','email', 'servicio']
       

        