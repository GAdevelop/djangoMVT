import email
from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_registro = models.DateField()


class Profesores(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=16)


class Estudiantes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Materias(models.Model):

    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField()