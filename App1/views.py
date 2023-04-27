from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse
from App1.forms import CursoFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def cursos(request):
    return render(request,'App1/cursos.html')
def profesores(request):
    return render(request,'App1/profesores.html')
def estudiantes(request):
    return render(request,'App1/estudiantes.html')
def entregables(request):
    return render(request,'App1/entregables.html')
def cursoFormulario(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
                  curso.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "App1/cursoFormulario.html", {"miFormulario": miFormulario})

