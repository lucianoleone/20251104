from django.contrib import admin
from django.urls import path
from inicio.views import inicio, crear_auto, listar_autos,ver_auto, ActualizarAuto, EliminarAuto
from inicio.views import otra #nos traemos la vista que hemos creado para poder llamarla desde

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('otra/', otra, name='otra'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path('ver-auto/<auto_id>', ver_auto, name='ver_auto'), 
    path('actualizar-auto/<pk>', ActualizarAuto.as_view(), name='actualizar'),
    path('eliminar-auto/<pk>', EliminarAuto.as_view(), name='eliminar'),
    path('listar-autos/', listar_autos, name='listar_autos'),
]