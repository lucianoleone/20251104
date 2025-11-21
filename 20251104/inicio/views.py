from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #es una clase
from django.contrib.auth.decorators import login_required #es un decorador
# Create your views here.

#esto con http response esta bueno para cosas chicas porque el codigo html se pone todo junto sin las facilidades de VSC
# def inicio(request):
#     return HttpResponse( "<h1>Hola Mundo, esta es la pagina de inicio</h1>")
def inicio(request):
    return render(request, 'inicio.html')
def otra(request):
    return render(request, 'otra.html')
@login_required
def crear_auto(request):  
    auto= None
    #Si viene por post sabemos que es el formulario creado
    if request.method == 'POST': 
        formulario= CrearAuto(request.POST, request.FILES)
        # Validamos el formulario
        if formulario.is_valid():
            info= formulario.cleaned_data #informacion limpia del formulario 
            # Cargamos la informacion del formulario en el modelo y por consiguiente en la BD  
            auto= Auto(marca=info.get('marca'), modelo=info.get('modelo'), imagen=info.get('imagen'))
            auto.save()
            return redirect('listar_autos') #redirigimos a la vista listar autos
    # Sino se muestra el formulario vacio
    else:
        formulario = CrearAuto()
        return render(request, 'crear_auto.html', {'formulario': formulario})

def ver_auto(request, auto_id):
    auto=Auto.objects.get(id=auto_id)
    return render(request, 'ver_auto.html', {'auto': auto})

class ActualizarAuto(UpdateView):
    model = Auto
    fields = ['marca', 'modelo', 'imagen']
    template_name = 'actualizar_auto.html'
    success_url = reverse_lazy('listar_autos')

class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = 'eliminar_auto.html'
    success_url = reverse_lazy('listar_autos')    
def listar_autos(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get('modelo')
        listado_de_autos = Auto.objects.filter(modelo__icontains=modelo_a_buscar)
    return render(request, 'listar_autos.html', {'listado_de_autos': listado_de_autos, 'formulario': formulario})

