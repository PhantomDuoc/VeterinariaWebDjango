from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Tipo de Usuario')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre del tipo de usuario')

    def __str__(self):
        return self.nombreCategoria


class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name='ID de Usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    passwordUsuario = models.CharField(max_length=50, verbose_name='Contraseña', min_length=8)
    categoria = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.idUsuario, self.nombreUsuario