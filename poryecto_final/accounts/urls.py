from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('ver_perfil/', ver_perfil, name='ver_perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar_password/', cambiar_password, name='cambiar_password'),
    path('logout/', cerrar_sesion, name='logout'),
    path('agregar_avatar/', agregar_avatar, name='AgregarAvatar'),
    path('eliminar_cuenta/',eliminar_cuenta, name='eliminar_cuenta'),
    path('eliminar_cualquier_cuenta/<int:user_id>/', eliminar_cualquier_cuenta, name='eliminar_cualquier_cuenta'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    ]