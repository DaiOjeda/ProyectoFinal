from django.db import models

class Grupo(models.Model):
    camada = models.CharField(max_length=8)
    nombre_lider = models.CharField(max_length=30)
    apellido_lider = models.CharField(max_length=30)

class Integrante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8)


