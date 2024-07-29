from AppAnni1 import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
]

clase_21 = [
        path('formulario/', views.formulario, name="Formulario"),
        path('buscar_form/', views.buscar_form, name="Buscar_Formulario")
]

urlpatterns += clase_21