from django.urls import path
from . import views



urlpatterns = [
    path("", views.inicio),
    path("estudiantes", views.estudiantes, name="estudiantes"),
    path("lista_estudiantes", views.lista_estudiantes),
    path("profesores", views.profesores, name="profesores"),
    path("familia", views.lista_familia),
    #path("contacto", views.contacto),
    path("alta_familiares", views.alta_familia),
    path("formulario_profesores", views.formulario_profes),
    path("formulario_estudiantes", views.formulario_est),
    path("buscar_estudiantes", views.buscar_est),
    path("buscar", views.buscar),
    path("materias", views.materias, name="materias"),
    path("formulario_materias", views.formulario_mat)
]
