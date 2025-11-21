from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid(): #en la validacion ya hace el chequeo de la existencia del usuario y todo lo necesario para saber que le usuario es valido
            usuario = formulario.get_user()
            #logueamos al usuario
            auth_login(request, usuario)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    return render(request, 'login.html', {"formulario": formulario})

def logout(request):
    return render(request, 'usuarios/logout.html')
def register(request):
    return render(request, 'usuarios/registro.html')