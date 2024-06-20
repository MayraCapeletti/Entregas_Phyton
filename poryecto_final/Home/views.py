
from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

def inicio(request):
    return render(request, 'inicio.html')