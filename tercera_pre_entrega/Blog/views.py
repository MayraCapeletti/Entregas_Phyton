from django.http import HttpResponse
from django.shortcuts import render
from .models import Autor, Categoria, Post
from . forms import PostFormulario, AutorFormulario, CategoriaFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

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

#CRUD DE POST
def crear_post(req):

    if req.method == 'POST':
        form = PostFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Post creado con éxito!"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        form = PostFormulario()
    return render(req, "crear_post.html", {'form': form})

class PostList(ListView):
    model = Post
    template_name = "lista_post.html"
    context_object_name = "post"

class PostDetail(DetailView):

  model = Post
  template_name = 'post_detail.html'
  context_object_name = "post"

class PostCreate(CreateView):

  model = Post
  template_name = 'crear_post.html'
  fields = ["nombre","contenido", "autor", "categoria"]
  success_url = "/blog/"

class PostUpdate(UpdateView):

  model = Post
  template_name = 'post_update.html'
  fields = ('__all__')
  success_url = "/blog/"
  context_object_name = "post"

class PostDelete(DeleteView):

  model = Post
  template_name = 'post_delete.html'
  success_url = "/blog/"
  context_object_name = "post"




#CRUD DE AUTOR
#leer
def lista_autores(req):
    autores = Autor.objects.all() #acá voy a guardar la respuesta de la consulta en la base de dato
    return render(req, "leer_autores.html", {"autores": autores}) #este último autor es de la variable q trae los datos de la base
#crear
def crear_autor(req):
    if req.method == 'POST':
        form = AutorFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Autor creado con éxito!"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        form = AutorFormulario()
    return render(req, "crear_author.html", {'form': form})
#borrar
def eliminar_autor(req, id):
    if req.method == 'POST' :
        autor= Autor.objects.get(id=id) #acá me trae el autor que tiene ese id
        autor.delete()
        autores = Autor.objects.all() 
        return render(req, "leer_autores.html", {"autores": autores})
#editar
def editar_autor(req, id):
    if req.method == 'POST':
        form = AutorFormulario(req.POST)
        if form.is_valid():
            data =form.cleaned_data
            autor= Autor.objects.get(id=id)
            autor.nombre = data['nombre']
            autor.bio = data['bio']

            autor.save()
            return render(req, "inicio.html", {"mensaje": "¡Autor actualizado con éxito!"})
        
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        autor= Autor.objects.get(id=id)
        form = AutorFormulario(initial={
            "nombre": autor.nombre,
             "bio": autor.bio
        })
        return render(req, "editar_autor.html", {'form': form, "id": autor.id})


def crear_categoria(req):
    if req.method == 'POST':
        form = CategoriaFormulario(req.POST)
        if form.is_valid():
            form.save()
            return render(req, "inicio.html", {"mensaje": "¡Categoría creada con éxito!"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
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



