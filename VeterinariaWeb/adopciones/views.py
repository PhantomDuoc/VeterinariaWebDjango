from django.shortcuts import render
from .models import enAdopcion

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

# Create your views here.
def home(request):
    mascotas = enAdopcion.objects.all()
    context = {
        'enAdopcion':mascotas
    }
    return render(request, 'adopciones/index.html', context)

def contacto(request):
    return render(request, 'adopciones/contacto.html')

def conocenos(request):
    return render(request, 'adopciones/conocenos.html')

def adopciones(request):
    mascotas = enAdopcion.objects.all()
    context = {
        'enAdopcion':mascotas
    }
    return render(request, 'adopciones/adopciones.html', context)

