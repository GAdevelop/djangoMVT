from re import A
from django.shortcuts import render
from usuarios.models import *
from django.http import HttpResponse
from django.template import loader
from usuarios.forms import *
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
    profesores = Profesores.objects.all()
    datos = {"datos" : profesores}

    return render(request, "profesores.html", datos)




def formulario_est(request):
    
    if request.method == "POST":
        
        mi_formulario = Formulario_estudiantes(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            estudiantes = Estudiantes(nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'])
            estudiantes.save()

            return render(request , "formulario_est.html")

    return render(request , "formulario_est.html")



def buscar_est(request):
    return render(request, "buscar_estudiantes.html")


def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        estudiantes = Estudiantes.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html" , {"estudiantes" : estudiantes} )
    else:
        return HttpResponse("Campo vacío")
    return HttpResponse(f"Se busca al estudiante: { request.GET['nombre']}")



def formulario_profes(request):
    
    if request.method == "POST":
        
        mi_formulario = Formulario_profesores(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profesores = Profesores(nombre=datos['nombre'], apellido=datos['apellido'], email=datos['email'], profesion=datos['profesion'])
            profesores.save()
            return render(request, "formulario_profes.html")

    return render(request, "formulario_profes.html")



def materias(request):
    materias = Materias.objects.all()
    datos = {"datos" : materias}

    return render(request, "materias.html", datos)


def formulario_mat(request):
    
    if request.method == "POST":
        
        mi_formulario = Formulario_materias(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            materias = Materias(nombre=datos['nombre'], camada=datos['camada'], fecha_de_inicio=datos['fecha_de_inicio'])
            materias.save()
            return render(request, "formulario_mat.html")

    return render(request, "formulario_mat.html")