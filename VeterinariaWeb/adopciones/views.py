from django.shortcuts import render
from .models import enAdopcion
from .forms import AdopcionForm

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

def form_adopcion(request):
    datos = {
        'form':AdopcionForm
    }
    if(request.method == 'POST'):
        formulario = AdopcionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
    return render(request,'adopciones/form_adopciones.html', datos)