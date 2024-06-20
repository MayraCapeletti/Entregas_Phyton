from django.urls import path
from Home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('inicio/', inicio, name='inicio'),
]