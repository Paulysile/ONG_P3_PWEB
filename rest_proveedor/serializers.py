from rest_framework import serializers
from core.models import Proveedores

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedores
        fields= ['rut','razonsocial','descripcion','telefono','email', 'servicio'] 