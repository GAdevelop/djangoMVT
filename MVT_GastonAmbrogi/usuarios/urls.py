from django.urls import path
from . import views



urlpatterns = [
    path("", views.inicio),
    path("Familia", views.lista_familia)
]
