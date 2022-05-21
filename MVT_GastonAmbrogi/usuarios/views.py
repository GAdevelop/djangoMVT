from django.shortcuts import render
from usuarios.models import Familia
import datetime
# Create your views here.


def inicio(request):
    
    return render(request , "index.html")



def lista_familia(request):

    miembros = Familia.objects.all()
    datos = {"datos" : miembros}

    return render(request, "lista_familiares.html", datos)