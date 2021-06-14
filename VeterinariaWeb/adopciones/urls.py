from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('conocenos', conocenos, name="conocenos"),
    path('adopciones', adopciones, name="adopciones"),
]