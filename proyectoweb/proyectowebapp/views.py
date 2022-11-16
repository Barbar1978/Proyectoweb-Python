from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request,"proyectowebapp/home.html")

def tienda (request):
    return render(request,"proyectowebapp/tienda.html")
   

def blog  (request):
    return render(request,"proyectowebapp/blog.html")
 

#def busqueda_productos(request):
    
    # return render (request , "busqueda_productos.html")
#def buscar(request):
   # mensaje="Articulo buscado :%r"%request.get ["prd"]
    #return HttpResponse