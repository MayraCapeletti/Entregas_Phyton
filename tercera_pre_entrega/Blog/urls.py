from django.urls import path
from Blog.views import crear_post_por_url,  lista_post, inicio, crear_post, crear_autor, crear_categoria, busqueda_post, busqueda_autor, buscar, buscar_por_autor, buscar_por_categoria, busqueda_categorias


urlpatterns = [
    path('agrega-post/<title>/<content>/<author>/<category>', crear_post_por_url),
    path('lista-post/', lista_post, name='lista_post'),
    path('', inicio, name='inicio'),
    path('crear_post', crear_post, name='crear_post'),
    path('crear_autor', crear_autor, name='crear_autor'),
    path('crear_categoria', crear_categoria, name='crear_categoria'),
    path('busqueda_post', busqueda_post, name='busqueda_post'),
    path('buscar', buscar, name='buscarPost'),
    path('busqueda_autor', busqueda_autor, name='busqueda_autor'),
    path('buscar_por_autor', buscar_por_autor, name='buscarAutor'),
    path('busqueda_categoria', busqueda_categorias, name='busqueda_categoria'),
    path('buscar_por_categoria', buscar_por_categoria, name='buscarCategoria'),

]
