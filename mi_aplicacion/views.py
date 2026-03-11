from django.shortcuts import render, redirect

from django.views import View

from mi_aplicacion.models import Escuela, Maestro

from mi_aplicacion.forms import EscuelaForm, MaestroForm

class home(View):
    def get(self , request):
        cdx={
            "titulo":"home",
            "subtitulo":"Bienvenido a mi primer aplicacion"
            }
        return render(request , "home/home.html", cdx)
    
class escuela(View):
    def get(self , request):
        escuelas = Escuela.objects.all()
        cdx={
            "titulo":"Escuelas",
            "subtitulo":"Lista de escuelas",
            "escuelas":escuelas
            }
        return render(request , "escuelas/escuelas.html", cdx)
    
class EscuelaAlta(View):
    def get(self , request ):
        form = EscuelaForm()
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Alta Escuela",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    def post(self , request):
        form = EscuelaForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
            return redirect("home")
    
class EscuelaEditar(View):
    def get(self , request , id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Editar Escuela",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    def post(self , request , id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST , request.FILES , instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")

class EscuelaEliminar(View):
    def get(self , request , id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Eliminacion Escuela",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    def post(self , request , id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST , request.FILES , instance=escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect("home")
    
        
class Maestros(View):
    def get(self , request):
        maestros = Maestro.objects.all()
        cdx={
            "titulo":"Maestro",
            "subtitulo":"Lista de maestros",
            "maestros":maestros
            }
        return render(request , "maestros/maestros.html", cdx)

class MaestroAlta(View):
    def get(self , request ):
        form = MaestroForm()
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Alta Maestro",
        "form":form
        }
        return render(request , 'maestros/CRUD.html', cdx)
# Create your views here.
