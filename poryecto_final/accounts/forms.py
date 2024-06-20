from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class FormularioRegistro(UserCreationForm):

    email     = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text="")
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput, help_text="")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), 
    required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model=User
    fields=["email", "first_name", "last_name"]
    help_texts = {k: '' for k in fields}

  def clean_password2(self):
    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password1 != password2:
      raise forms.ValidationError("Las contraseñas deben ser iguales")
    return password2
  
  def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        password1 = self.cleaned_data.get("password1")

        if password1:
            user.set_password(password1)

        if commit:
            user.save()
        return user

class FormularioCambiarPassword(PasswordChangeForm):

    old_password  = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password nuevo')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Confirmar password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}
  
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']