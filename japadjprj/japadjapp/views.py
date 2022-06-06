from django.shortcuts import render;
from django.http import HttpResponse;
#  # first
# import models;

# second
import time
from .models import Usuario, Libro, Categoria
# Create your views here.

def index(request):
    return render(request, "japadjapp/index.html")



def login(request):
    return HttpResponse("Llegamos al inicio de sesion")

def procesar(request):
    if request.method == 'POST':
        user = request.POST['usuario']
        contra = request.POST['clave']
        
        print(f"Usuario: {user}, Clave: {contra}")
    try:
        #comparamos el usuario y clave del front end con el de la base de datos
        usr = Usuario.objects.get(usuario = user, clave = contra);
        categorias = Categoria.objects.all()
        libros = Libro.objects.all()
        
        contexto = {
            "categorias" : categorias,
            "libros" : libros,
            "usuario" : usr
        }
        
        return render(request, "japadjapp/admin_startpage.html",{"contexto": contexto})
    
    except Usuario.DoesNotExist:
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"japadjapp/incorrecto.html",{"mensaje": mensaje})
        
    # return render(request, "japadjapp/correcto.html", {"mensaje": mensaje})
    
    
def editar_categoria(request):
    return HttpResponse("Editando ...")

def eliminar_categoria(request):
    return HttpResponse("Eliminando ...")