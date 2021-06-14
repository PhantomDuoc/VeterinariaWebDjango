from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

# Create your views here.
def home(request):
    lista = ["Lasagna","Charqui", "Porotos"]
    context = {"nombre":"Hugo Cerda","comidas":lista}
    return render(request, 'adopciones/index.html',context)

def contacto(request):
    return render(request, 'adopciones/contacto.html')

def conocenos(request):
    return render(request, 'adopciones/conocenos.html')

def adopciones(request):
    return render(request, 'adopciones/adopciones.html')

