from django import forms
from .models import Autor, Categoria, Post


class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'bio']


class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']
