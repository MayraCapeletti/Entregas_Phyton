from django.http import HttpResponse
from django.shortcuts import render
from .models import Autor, Categoria, Post
from . forms import PostFormulario, AutorFormulario, CategoriaFormulario

# Create your views here.


# Crear un post utilizando parámetros en la UR
def crear_post_por_url(req, titulo, contenido, autor, categoria):

    nuevo_post = Post(titulo=titulo, contenido=contenido,
                      autor=autor, categoria=categoria)
    nuevo_post.save()

    return HttpResponse(f"""
      <p>El post {nuevo_post.title} fue creado!</p>
    """)


def lista_post(req):

    lista = Post.objects.all()

    return render(req, "lista_post.html", {"lista_post": lista})


def inicio(req):

    return render(req, "inicio.html", {})


def crear_post(req):

    if req.method == 'POST':
        form = PostFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Post creado con éxito!"})
    else:
        form = PostFormulario()
    return render(req, "crear_post.html", {'form': form})


def crear_autor(req):
    if req.method == 'POST':
        form = AutorFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Autor creado con éxito!"})
    else:
        form = AutorFormulario()
    return render(req, "crear_author.html", {'form': form})


def crear_categoria(req):
    if req.method == 'POST':
        form = CategoriaFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Categoría creada con éxito!"})
    else:
        form = CategoriaFormulario()
    return render(req, "crear_categoria.html", {'form': form})


def busqueda_post(req):
    return render(req, "busqueda_post.html", {})

# Busqueda de post por titulo


def buscar(req):
    if 'post' in req.GET:
        query = req.GET['post']
        results = Post.objects.filter(titulo__icontains=query)
        return render(req, "resultado_busqueda.html", {"results": results})
    else:
        return render(req, "inicio.html", {"mensaje": "No enviase el dato"})

# Página de búsqueda de autores


def busqueda_autor(req):
    return render(req, "busqueda_autor.html", {})

# Buscar posts por autor


def buscar_por_autor(req):
    if 'autor' in req.GET:
        autor_nombre = req.GET['autor']
        autor = Autor.objects.filter(nombre__icontains=autor_nombre).first()
        if autor:
            results = Post.objects.filter(autor=autor)
            return render(req, "resultado_busqueda_autor.html", {"results": results, "autor": autor})
        else:
            return render(req, "resultado_busqueda_autor.html", {"results": [], "mensaje": "No se encontraron autores con ese nombre"})
    else:
        return render(req, "inicio.html", {"mensaje": "No enviaste el dato"})

# Página de búsqueda de categorias


def busqueda_categorias(req):
    return render(req, "busqueda_categorias.html", {})

# Buscar posts por categoria


def buscar_por_categoria(req):
    if 'categoria' in req.GET:
        categoria_nombre = req.GET['categoria']
        categoria = Categoria.objects.filter(
            nombre__icontains=categoria_nombre).first()
        if categoria:
            results = Post.objects.filter(categoria=categoria)
            return render(req, "resultado_busqueda_categoria.html", {"results": results, "categoria": categoria})
        else:
            return render(req, "resultado_busqueda_categoria.html", {"results": [], "mensaje": "No se encontraron categorias con ese nombre"})
    else:
        return render(req, "inicio.html", {"mensaje": "No enviaste el dato"})
