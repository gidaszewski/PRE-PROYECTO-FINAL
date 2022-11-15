from django.db import models

class Lanzamientos(models.Model):

    nombre_del_lanzamiento=models.CharField(max_length=40)
    fecha_de_lanzamiento=models.DateField()
    incluye=models.CharField(max_length=40)

class Inscripcion(models.Model):

    nombre=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    contraseña=models.CharField(max_length=40)

class Programa(models.Model):

    nombre=models.CharField(max_length=40)
    clase=models.IntegerField()
    informacion=models.CharField(max_length=40)