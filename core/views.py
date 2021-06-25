from django.shortcuts import render



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