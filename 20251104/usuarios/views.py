from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from usuarios.forms import FormularioRegistroUsuario


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


def register(request):
        if request.method == 'POST':
            formulario = FormularioRegistroUsuario(request.POST)
            if formulario.is_valid(): #en la validacion ya hace el chequeo de la existencia del usuario y todo lo necesario para saber que le usuario es valido
                formulario.save()  #guardamos el usuario y se crea el usuario
                return redirect('login')
        else:
            formulario = FormularioRegistroUsuario()
        return render(request, 'register.html', {"formulario": formulario})