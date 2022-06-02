import email
from django import forms


class Formulario_estudiantes(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class Formulario_profesores(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=16)

class Formulario_materias(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    fecha_de_inicio = forms.DateField()