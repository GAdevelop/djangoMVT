from re import A
from django.shortcuts import render
from usuarios.models import *
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.


def inicio(request):
    
    return render(request , "index.html")



def lista_familia(request):

    miembros = Familia.objects.all() #trae los datos de familia
    datos = {"datos" : miembros} #mete los datos en un diccionario

    return render(request, "lista_familiares.html", datos) # se crea un html con esos datos y se rederiza para ser mostrado


#esta es una manera de crear data en la lista de la BD
def alta_familia(request):
    
    familiar = Familia(nombre = "Marcos Rodriguez", dni=42969111, fecha_registro=datetime.datetime(2021,5,10))
    familiar.save()
    familiar = Familia(nombre = "Pamela Rodriguez", dni=40276001, fecha_registro=datetime.datetime(2020,1,25))
    familiar.save()
    familiar = Familia(nombre = "Tomas Rodriguez", dni=40007301, fecha_registro=datetime.datetime(2021,5,4))
    familiar.save()

    return HttpResponse("Todo ok.")




""" def estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    diccionario = {"Estudiantes" : {estudiantes}}
    plantilla = loader.get_template("estudiantes.html")
    documento = plantilla.render(diccionario)
    return render(request, documento) """


""" def lista_estudiantes(request, nombre, apellido):
    lista = Estudiantes(nombre=nombre, apellido=apellido)
    lista.save()
    return render(request) """

def estudiantes(request):

    alumnos = Estudiantes.objects.all()
    datos = {"datos" : alumnos}

    return render(request, "estudiantes.html", datos)


def lista_estudiantes(request):
    
    alumno = Estudiantes(nombre = "Martina", apellido="Gutierrez", email="martugutierrez@gmail.com")
    alumno.save()
    alumno = Estudiantes(nombre = "Juan", apellido="Navarro", email="juan.navarro@hotmail.com")
    alumno.save()
    alumno = Estudiantes(nombre = "Bautista", apellido="Copper", email="bautistacopper@yahoo.com.ar")
    alumno.save()

    return HttpResponse(request)





def contacto(request):
    
    return render(request , "contacto.html")



def profesores(request):
    
    return render(request , "profesores.html")