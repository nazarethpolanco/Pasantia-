from django.urls import path

from .views import ListarLibro

urlpatterns = [
    path('', ListarLibro.as_view()),
]
