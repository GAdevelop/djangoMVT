from django.shortcuts import render
from usuarios.models import Familia
from django.http import HttpResponse
import datetime
# Create your views here.


def inicio(request):
    
    return render(request , "index.html")



def lista_familia(request):

    miembros = Familia.objects.all() #trae los datos de familia
    datos = {"datos" : miembros} #mete los datos en un diccionario

    return render(request, "lista_familiares.html", datos) # se crea un html con esos datos y se rederiza para ser mostrado



def alta_familia(request):
    
    familiar = Familia(nombre = "Marcos Rodriguez", dni=42969111, fecha_registro=datetime.datetime(2021,5,10))
    familiar.save()
    familiar = Familia(nombre = "Pamela Rodriguez", dni=40276001, fecha_registro=datetime.datetime(2020,1,25))
    familiar.save()
    familiar = Familia(nombre = "Tomas Rodriguez", dni=40007301, fecha_registro=datetime.datetime(2021,5,4))
    familiar.save()

    return HttpResponse("Todo ok.")