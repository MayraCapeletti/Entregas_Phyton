from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.views.generic.edit import FormMixin


# Create your views here.
def ver_posts(request):
    posts = Post.objects.all().order_by('id')
    return render(request, 'ver_posts.html', { 'posts' : posts })


class PostList(ListView):
    model = Post
    template_name = "lista_post.html"
    context_object_name = "posts"

class PostDetail(FormMixin, DetailView):

  model = Post
  template_name = 'post_detail.html'
  context_object_name = "post"
  form_class = CommentForm

  def get_success_url(self):
        return self.request.path  # Redirige a la misma página de detalle después de enviar el comentario

  def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.object
            new_comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.filter(active=True)
        return context

class PostCreate(LoginRequiredMixin, CreateView):

  model = Post
  template_name = 'crear_post.html'
  fields = ['title', 'subtitle', 'body', 'image']
  success_url = "/post/"

  def form_valid(self, form):
        form.instance.author = self.request.user  # Asigna el usuario actual como autor del post
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):

  model = Post
  template_name = 'post_update.html'
  fields = ('__all__')
  success_url = "/post/"
  context_object_name = "post"

class PostDelete(LoginRequiredMixin, DeleteView):

  model = Post
  template_name = 'post_delete.html'
  success_url = "/post/"
  context_object_name = "post"


def busqueda_post(req):
    return render(req, "busqueda_post.html", {})

def buscar(req):
    if 'post' in req.GET:
        query = req.GET['post']
        results = Post.objects.filter(titulo__icontains=query)
        return render(req, "resultado_busqueda.html", {"results": results})
    else:
        return render(req, "inicio.html", {"mensaje": "No enviaste el dato"})