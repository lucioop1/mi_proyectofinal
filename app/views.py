from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Alumno
from .forms import LibroForm, AlumnoForm


def inicio(request):
    total_libros = Libro.objects.count()
    total_alumnos = Alumno.objects.count()
    return render(request, 'inicio.html', {
        'total_libros': total_libros,
        'total_alumnos': total_alumnos
    })

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})


def panel_general(request):
    # Cantidad total de libros disponibles
    libros_disponibles = Libro.objects.filter(disponible=True).count()
    # Promedio de edad de los alumnos (puede ser None si no hay alumnos)
    from django.db.models import Avg
    promedio_edad = Alumno.objects.aggregate(avg=Avg('edad'))['avg']
    # Tres libros más recientes por año de publicación
    ultimos_tres = Libro.objects.order_by('-anio_publicacion')[:3]

    return render(request, 'panel_general.html', {
        'libros_disponibles': libros_disponibles,
        'promedio_edad': promedio_edad,
        'ultimos_tres': ultimos_tres,
    })