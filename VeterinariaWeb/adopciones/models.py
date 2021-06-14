from django.db import models

# Create your models here.

class EstadoAdopcion(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID Estado')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre del estado de la adopcion')

    def __str__(self):
        return self.nombreCategoria


class enAdopcion(models.Model):
    idRescatado = models.IntegerField(primary_key=True, verbose_name='ID del animal rescatado dado en adopcion')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    especie = models.CharField(max_length=50, verbose_name='Especie del animal')
    raza = models.CharField(max_length=50, verbose_name='Raza del animal')
    estado = models.ForeignKey(EstadoAdopcion, on_delete=models.CASCADE)

    def __str__(self):
        return self.idUsuario, self.nombreUsuario