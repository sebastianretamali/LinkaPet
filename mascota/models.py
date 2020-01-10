from django.db import models
from django.contrib.auth.models import User

SEXO = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )

TIPO = (
        ('Gato', 'Gato'),
        ('Perro', 'Perro'),
    )

ESTADO = (
        ('Adulto', 'Adulto'),
        ('Cachorro', 'Cachorro'),
    )

TAMA = (
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    )

PERSO = (
        ('Timido', 'Timido'),
        ('Tranquilo', 'Tranquilo'),
        ('Dormilon', 'Dormilon'),
        ('Jugueton', 'Jugueton'),
        ('Mañoso', 'Mañoso'),
    )


    
class Mascota(models.Model):
    img = models.ImageField(upload_to='imgp/')
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    raza = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=SEXO)
    tipo = models.CharField(max_length=10, choices=TIPO)
    estado = models.CharField(max_length=10, choices=ESTADO)
    tamano = models.CharField(max_length=10, choices=TAMA)
    personalidad = models.CharField(max_length=10, choices=PERSO)
    descripcion = models.TextField(max_length=500)
    fundacion = models.CharField(max_length=25)
    usuario = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    mail_fundacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
   
