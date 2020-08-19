from django.db import models

# Create your models here.
class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=254)

    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=254)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete= models.CASCADE)
    documento = models.IntegerField()
    lugarresidencia = models.ForeignKey(Ciudad, on_delete= models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=12)
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre