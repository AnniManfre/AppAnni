from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
from AppAnni1.forms import Formulario, BuscaCursoForm


def inicio(request):
    return render(request, "AppAnni1/index.html")

def cursos(request):
    return render(request, "AppAnni1/cursos.html")

def profesores(request):
    return render(request, "AppAnni1/profesores.html")

def estudiantes(request):
    return render(request, "AppAnni1/estudiantes.html")

def entregables(request):
    return render(request, "AppAnni1/entregables.html")

def formulario(request):
    if request.method == "POST":
        mi_formulario = Formulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "AppAnni1/index.html")
    else:
        mi_formulario = Formulario()

    return render(request, "AppAnni1/formulario.html", {"mi_formulario": mi_formulario})

def buscar_form(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppAnni1/buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppAnni1/buscar_form.html", {"miFormulario": miFormulario})

