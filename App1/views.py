from django.shortcuts import render
from App1.models import Curso, Profesor
from django.http import HttpResponse
from App1.forms import CursoFormulario, ProfesorFormulario

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

def profesorFormulario(request):
     if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Profesor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ProfesorFormulario()
             
     return render(request, "App1/profesorFormulario.html", {"miFormulario": miFormulario})