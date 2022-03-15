from django.db import models


class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    natalicio = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'El autor se llama: {self.nombre}'

   
