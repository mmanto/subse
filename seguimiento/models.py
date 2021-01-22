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


class FuenteInversion(models.Model):

    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class TipoEstado(models.Model):

    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Registro(models.Model):

    id_tipo_accion = models.ForeignKey(TipoAccion, null=True, blank=True, on_delete=models.CASCADE)

    id_tipo_estado = models.ForeignKey(TipoEstado, null=True, blank=True, on_delete=models.CASCADE)

    id_municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)

    cantidad = models.IntegerField(default = 0, blank = True)

    id_fuente_inversion =  models.ForeignKey(FuenteInversion, null=True, blank=True, on_delete=models.CASCADE)

    id_programa = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)

    monto = models.CharField(max_length=10)

    anio = models.CharField(max_length=10)
    
    def __str__(self):
        return self.anio