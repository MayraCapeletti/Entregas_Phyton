from django.urls import path
from Post.views import *

urlpatterns = [
    path('', ver_posts, name='ver_posts'),
    path('lista-post/<int:start>', PostList.as_view(), name='ListaPost'),
    path('detalle-post/<pk>', PostDetail.as_view(), name='DetallePost'),
    path('crea-post/', PostCreate.as_view(), name='CreaPost'),
    path('actualiza-post/<pk>', PostUpdate.as_view(), name='ActualizaPost'), # type: ignore
    path('elimina-post/<int:pk>', PostDelete.as_view(), name='EliminaPost'),
    path('busqueda_post', busqueda_post, name='busqueda_post'),
    path('buscar', buscar, name='buscarPost'),
    
    ]