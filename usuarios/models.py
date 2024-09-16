from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.TextField(max_length=100)
    apellidoMaterno = models.TextField(max_length=100)
    edad = models.IntegerField()
    nombreCuenta= models.TextField(max_length=100, unique=True)
    contrasena = models.TextField(max_length=100)

    def __str__(self):
        return self.nombreCuenta