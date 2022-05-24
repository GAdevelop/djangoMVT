from django.urls import path
from . import views



urlpatterns = [
    path("", views.inicio),
    path("familia", views.lista_familia),
    path("alta_familiares", views.alta_familia)
]
