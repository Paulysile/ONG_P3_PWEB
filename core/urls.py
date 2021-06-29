from django.urls import path
from .import views
from .views import  inicio, contacto, formulario, enviado, exitoso, gatos, perros, proveedores, form_prov, form_mod_prov, form_del_prov


urlpatterns = [
    
    path('', inicio, name="inicio"),
    path('contacto', contacto, name="contacto"),
    path('formulario', formulario, name="formulario"),
    path('formulario-enviado', enviado, name="enviado"),
    path('login-exitoso', exitoso, name="exitoso"),
    path('seccion-gatos', gatos, name="gatos"),
    path('seccion-perros', perros, name="perros"),
    path('proveedores', proveedores, name="proveedores"),
    path('form_prov', form_prov, name="form_prov"),
    path('form_mod_prov/<id>', form_mod_prov, name="form_mod_prov"),
    path('form_del_prov/<id>', form_del_prov, name="form_del_prov"),
]

