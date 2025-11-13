from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_libros/', views.lista_libros, name='lista_libros'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('panel/', views.panel_general, name='panel_general'),
]