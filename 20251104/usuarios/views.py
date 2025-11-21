from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def login(request):
    formulario =AuthenticationForm()  # Aquí iría la lógica para manejar el formulario de login
    return render(request, 'login.html')
def logout(request):
    return render(request, 'usuarios/logout.html')
def register(request):
    return render(request, 'usuarios/registro.html')