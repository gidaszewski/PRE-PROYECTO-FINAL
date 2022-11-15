from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from django.template import loader
from App.forms import *

def home(request):
    return render(request, 'App/inicio.html')

def info_personal(request):
    return render(request, 'App/informacion.html')

def buscar_tracks(request):

    biblioteca=Lanzamientos.objects.all()

    datos_de_tracks={"biblioteca": biblioteca}

    plantilla = loader.get_template("App/biblioteca.html")

    documento =  plantilla.render(datos_de_tracks)

    return HttpResponse(documento)

def resultados_busqueda_canciones(request):

    nombre_del_lanzamiento = request.GET["nombre_del_lanzamiento"]

    canciones = Lanzamientos.objects.filter(nombre_del_lanzamiento__icontains=nombre_del_lanzamiento)

    return render(request, "App/resultados_busqueda.html", {"canciones": canciones}) 

def creacion_usuario(request):

    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            inscripcion = Inscripcion(
                nombre=data["nombre"], email=data["email"], contraseña=data["contraseña"])

            inscripcion.save()
            
        return render(request, 'App/toolz.html')

    else:
        formulario = UsuarioFormulario()
    contexto = {"formulario": formulario}
    return render(request, "App/creacionToolz.html", contexto)

def programa_de_clases(request):

    programa=Programa.objects.all()

    info_de_temas={"programa": programa}

    plantilla = loader.get_template("App/toolz.html")

    documento =  plantilla.render(info_de_temas)

    return HttpResponse(documento)

def resultado_busqueda_programa(request):

    nombre_del_tema = request.GET["nombre_del_tema"]

    temas = Programa.objects.filter(nombre__icontains=nombre_del_tema)

    return render(request, "App/busqueda_programa.html", {"temas": temas})
    