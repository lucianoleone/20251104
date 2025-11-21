from django.urls import path
from usuarios.views import login, logout, registro
urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('register/',registro, name='registro')
]
