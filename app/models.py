from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    anio_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
