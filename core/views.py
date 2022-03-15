from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Libro


class ListarLibro(ListView):
    model = Libro
    template_name = 'index.html'

