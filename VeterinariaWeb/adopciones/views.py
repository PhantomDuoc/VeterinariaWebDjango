from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'adopciones/index.html')

def contact(request):
    return render(request, 'adopciones/contacto.html')

def conocenos(request):
    return render(request, 'adopciones/conocenos.html')

def adopciones(request):
    return render(request, 'adopciones/adopciones.html'),

