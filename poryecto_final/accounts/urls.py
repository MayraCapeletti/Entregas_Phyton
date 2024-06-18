from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('ver_perfil/', ver_perfil, name='ver_perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar_password/', cambiar_password, name='cambiar_password'),
    path('logout/', cerrar_sesion, name='logout'),
    ]