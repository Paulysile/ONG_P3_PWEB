from django.shortcuts import render, redirect
from .models import Proveedores
from .forms import ProveedorForm


def inicio(request):
    return render (request,'core/index.html')

def contacto(request):
    return render (request,'core/contacto.html')

def enviado(request):
    return render (request,'core/formulario-enviado.html')

def formulario(request):
    return render (request,'core/formulario.html')

def exitoso(request):
    return render (request,'core/login-exitoso.html')

def gatos(request):
    return render (request,'core/seccion-gatos.html')

def perros(request):
    return render (request,'core/seccion-perros.html')

def proveedores(request):
    proveedores= Proveedores.objects.all()
    datos= {
        'proveedores': proveedores
    }
    return render(request, 'core/proveedores.html',datos)

def form_prov(request):
    datos= {
        'formulario': ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
                formulario.save()
                datos['mensaje'] = "Proveedor agregado exitosamente"
    return render(request, 'core/form_prov.html',datos)

def form_mod_prov (request, id):
    proveedor= Proveedores.objects.get(rut=id)
    datos={
        'formulario': ProveedorForm(instance=proveedor)
    }
    if request.method=='POST':
        formulario= ProveedorForm(data=request.POST, instance= proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Proveedor modificado exitosamente"
    return render(request, 'core/form_mod_prov.html', datos)    

def form_del_prov (request, id):
    proveedor= Proveedores.objects.get(rut=id)
    proveedor.delete()
    
    return redirect(to="proveedores")