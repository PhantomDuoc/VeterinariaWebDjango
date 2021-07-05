from django.urls import path
from .views import lista_adopciones, detalle_adopciones

urlpatterns = [
    path('lista_adopciones', lista_adopciones, name="lista_adopciones"),
    path('detalle_adopciones/<id>',detalle_adopciones,name='detalle_adopciones'),
]