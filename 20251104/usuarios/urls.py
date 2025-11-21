from django.urls import path
from django.contrib import admin
from usuarios.views import login, logout, register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('register/',register, name='register')
]
