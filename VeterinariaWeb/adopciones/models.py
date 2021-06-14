from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID de Usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    passwordUsuario = models.CharField(max_length=50, verbose_name='Contraseña')

    def __str__(self) -> str:
        return self.nombreUsuario
