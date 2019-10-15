from django.db import models


SEXO = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )

TIPO = (
        ('G', 'Gato'),
        ('P', 'Perro'),
    )

ESTADO = (
        ('A', 'Adulto'),
        ('C', 'Cachorrro'),
    )


    
class Mascota(models.Model):
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField()
    raza = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=SEXO)
    tipo = models.CharField(max_length=1, choices=TIPO)
    estado = models.CharField(max_length=1, choices=ESTADO)
    tamano = models.CharField(max_length=10)
    img = models.ImageField(upload_to='imgp/')
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre

