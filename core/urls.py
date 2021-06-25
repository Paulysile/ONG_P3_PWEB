from django.urls import path
from .views import  inicio, contacto, formulario, enviado, exitoso, gatos, perros


urlpatterns = [
    
    path('', inicio, name="inicio"),
    path('contacto', contacto, name="contacto"),
    path('formulario', formulario, name="formulario"),
    path('formulario-enviado', enviado, name="enviado"),
    path('login-exitoso', exitoso, name="exitoso"),
    path('seccion-gatos', gatos, name="gatos"),
    path('seccion-perros', perros, name="perros"),
]

