from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from .forms import  UserEditForm, FormularioCambiarPassword, FormularioRegistro, AvatarForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from .models import Avatar

def login_view(req):
  if req.method == 'POST':
    miFormulario = AuthenticationForm(req, data=req.POST)
    if miFormulario.is_valid():
      data = miFormulario.cleaned_data
      usuario = data["username"]
      psw = data["password"]
      user = authenticate(username=usuario, password=psw)

      if user:
        login(req, user)
        return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
      else:
        return render(req, "inicio.html", {"mensaje": "Datos erroneos"})   
    else:
      return render(req, "inicio.html", {"mensaje": "Datos inválidos"}) 
  else:
    miFormulario = AuthenticationForm()
    return render(req, "login.html", {"miFormulario": miFormulario})
  
def register(req):
    if req.method == 'POST':
        formulario_registro = FormularioRegistro(req.POST)
        if formulario_registro.is_valid():
            data = formulario_registro.cleaned_data
            usuario = data["username"]
            formulario_registro.save()
            messages.success(req, f"Usuario {data['username']} creado con éxito!")
            return redirect('inicio')  # Redirige a una página donde se pueda ver el mensaje de éxito   
        else:
            messages.error(req, "Datos inválidos")
            return render(req, "registro.html", {"formulario_registro": formulario_registro})
    else:
        formulario_registro = FormularioRegistro()
        return render(req, "registro.html", {"formulario_registro": formulario_registro})
    
@login_required
def ver_perfil(request):
    try:
        avatar = request.user.avatar
    except Avatar.DoesNotExist:
        avatar = None

    context = {
        'avatar': avatar,
    }
    return render(request, 'perfil.html', context)
    

@login_required()
def editar_perfil(req):
  usuario = req.user
  if req.method == 'POST':
    miFormulario = UserEditForm(req.POST, instance=req.user)
    
    if miFormulario.is_valid():
      data = miFormulario.cleaned_data

      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password1"])
      usuario.save()
      update_session_auth_hash(req, usuario)  # Importante para mantener la sesión activa
      messages.success(req, 'Datos actualizados con éxito')
      return redirect(reverse_lazy('home')) 
      
    else:
      messages.error(req, 'Por favor, corrija los errores a continuación.')
      return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
  
  else:
    miFormulario = UserEditForm(instance=req.user)
    return render(req, "editar_perfil.html", {"miFormulario": miFormulario})

@login_required
def cambiar_password(req):
    if req.method == 'POST':
        formulario_cambio_password = FormularioCambiarPassword(req.user, req.POST)
        if formulario_cambio_password.is_valid():
            user = formulario_cambio_password.save()
            update_session_auth_hash(req, user)  # Importante para mantener la sesión activa
            messages.success(req, 'Tu contraseña ha sido actualizada con éxito.')
            return redirect(('ver_perfil'))
        else:
            messages.error(req, 'Por favor, corrija los errores a continuación.')
            return render(req, "cambiar_password.html", {"formulario_cambio_password": formulario_cambio_password})
    else:
        formulario_cambio_password = FormularioCambiarPassword(req.user)
    return render(req, 'cambiar_password.html', {"formulario_cambio_password": formulario_cambio_password})

@login_required
def cerrar_sesion(request):
    messages.add_message(request, messages.SUCCESS, '¡Has cerrado sesión! ¡Hasta luego!')
    logout(request)
    return redirect('inicio')

def agregar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, request.FILES)
        if avatar_form.is_valid():
            if avatar:
                avatar.imagen = avatar_form.cleaned_data['imagen']
                messages.success(request, "Avatar actualizado con éxito")
            else:
                avatar = Avatar(user=request.user, imagen=avatar_form.cleaned_data['imagen'])
                messages.success(request, "Avatar cargado con éxito")
            avatar.save()
            return redirect('inicio')  # Ajusta 'inicio' a la URL de tu página de inicio
        else:
            messages.error(request, "Datos inválidos")
    else:
        avatar_form = AvatarForm()

    return render(request, "agregar_avatar.html", {"avatar_form": avatar_form, "avatar": avatar})

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        return redirect('home')
    return render(request, 'confirmar_eliminacion.html')

User = get_user_model()
@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_cualquier_cuenta(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        if user.is_staff:
            messages.error(request, 'No puedes eliminar la cuenta de otro miembro del staff.')
        else:
            user.delete()
            messages.success(request, 'La cuenta ha sido eliminada con éxito.')
        return redirect('listar_usuarios')
    return render(request, 'confirmar_eliminacion.html', {'user_to_delete': user})

@login_required
@user_passes_test(lambda u: u.is_staff)
def listar_usuarios(request):
    users = User.objects.all()
    return render(request, 'listar_usuarios.html', {'users': users})