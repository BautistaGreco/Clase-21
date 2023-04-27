from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

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
      if request.method == 'POST':
            curso =  Curso(request.post['nombre'],(request.post['curso']))
            curso.save()
            return render(request, "App1/inicio.html")
      return render(request,"App1/cursoFormulario.html")

