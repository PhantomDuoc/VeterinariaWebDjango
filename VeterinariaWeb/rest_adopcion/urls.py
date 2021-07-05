from django.urls import path
from .views import lista_adopciones

urlpatterns = [
    path('lista_adopciones', lista_adopciones, name="lista_adopciones"),
     path('detalle-adopciones/<id>',detalle_adopciones,name='detalle_adopciones'),
]