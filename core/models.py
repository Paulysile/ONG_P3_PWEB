
from django.db import models
from rest_framework.fields import ReadOnlyField

class Servicio(models.Model):
    idServicio= models.IntegerField(primary_key= True, verbose_name='Id de Servicio' )
    nombreServicio = models.CharField(max_length= 100, verbose_name= 'Servicio')


    def __str__(self):
        return self.nombreServicio

class Proveedores(models.Model):
    rut= models.CharField(max_length=10, primary_key=True, verbose_name='RUT')
    razonsocial= models.CharField(max_length= 100, verbose_name= 'Razon Social')
    descripcion= models.CharField(max_length=200, null= True, blank=True, verbose_name='Descripcion')
    telefono= models.CharField(max_length=12, null= True, blank=True, verbose_name='Telefono')
    email= models.EmailField(max_length=100, null= True, blank=True, verbose_name='E-mail')
    servicio= models.ForeignKey(Servicio, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.rut
