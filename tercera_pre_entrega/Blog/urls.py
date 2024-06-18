from django.urls import path
from Blog.views import *

urlpatterns = [
    path('agrega-post/<title>/<content>/<author>/<category>', crear_post_por_url),
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
    path('lista-autores', lista_autores, name='listaAutores'),
    path('elimina-autor/<int:id>', eliminar_autor, name='eliminaAutor'),
    path('editar-autor/<int:id>', editar_autor, name='editaAutor'),
    path('lista-post/', PostList.as_view(), name='ListaPost'),
    path('detalle-post/<pk>', PostDetail.as_view(), name='DetallePost'),
    path('crea-post/', PostCreate.as_view(), name='CreaPost'),
    path('actualiza-post/<pk>', PostUpdate.as_view(), name='ActualizaPost'),
    path('elimina-post/<pk>', PostDelete.as_view(), name='EliminaPost'),

]
