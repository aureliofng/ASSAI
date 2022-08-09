from pickle import TRUE
from tkinter.tix import MAX
from turtle import RawTurtle
from django.db import models


##from django.core import serializers


class Tiposdocumentos(models.Model):
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.desc

    def natural_key(self):
        return (self.desc)

class Tiposformaciones (models.Model):
    desc = models.CharField(max_length=30)

    def __str__(self):
        return self.desc

    def natural_key(self):
        return (self.desc)

class Formacion(models.Model):
    tipo_formacion = models.ForeignKey(Tiposformaciones, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=300)
    horas = models.PositiveSmallIntegerField()
    vigencia_dias = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return (self.nombre, self.vigencia_dias)

class Departamentos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre) 
    
class Municipios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
            
    def natural_key(self):
        return (self.nombre)
 
class Estudiante(models.Model):
    id_estudiante =  models.PositiveBigIntegerField()
    tipo_doc = models.ForeignKey(Tiposdocumentos, on_delete=models.CASCADE)
    nombre_1 = models.CharField(max_length=30)
    nombre_2 = models.CharField(max_length=30)
    apellido_1 = models.CharField(max_length=30)
    apellido_2 = models.CharField(max_length=30)
    municipio = models.ForeignKey(Municipios, on_delete=models.CASCADE)
    celular = models.PositiveIntegerField()
    f_nacimiento = models.DateField()
    def __str__(self):
        texto="{0} {1} ({2})"
        return texto.format(self.nombre_1, self.apellido_1, self.id_estudiante)
    
    def natural_key(self):
        return (self.nombre_1, self.nombre_2, self.apellido_1, self.apellido_2)

class Certificado(models.Model):
    id_certificado = models.CharField(primary_key=True, max_length=10, editable=False)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_formacion = models.ForeignKey(Formacion, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_vencimiento = models.DateField()
    def __str__(self):
        return self.id_certificado