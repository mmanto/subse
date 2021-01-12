from django.db import models

# Create your models here.
class EntidadPropietaria(models.Model):
    
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class TipoAccion(models.Model):

    nombre = models.CharField(max_length=200)

    concepto = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):

    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Programa(models.Model):

    nombre = models.CharField(max_length=200)

    anio = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre


class TipoEstado(models.Model):

    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre