from django.db import models


PERSO = (
        ('ME', 'Muy extrovertido'),
        ('E', 'Extrovertido'),
        ('N', 'Neutral'),
        ('I', 'Introvertido'),
        ('MI', 'Muy introvertido'),
    )

NINOS = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'Más de 5'),
    )

DEPOR = (
        ('0', 'Ningún día'),
        ('1', 'Un día'),
        ('2', 'Dos días'),
        ('3', 'Tres días'),
        ('4', 'Cuatro días'),
        ('5', 'Cinco días'),
        ('6', 'Seis días'),
        ('7', 'Siete días'),
    )

VIVIENDA = (
        ('C', 'Casa con patio'),
        ('DC', 'Dpto Chico o Mediano'),
        ('DG', 'Dpto Grande'),
        ('P', 'Parcela'),
    )


class Cuestionario(models.Model):
    img = models.ImageField(upload_to='imgp/')
    personalidad = models.CharField(max_length=2, choices=PERSO)
    cant_ninos = models.CharField(max_length=1, choices=NINOS)
    edad = models.IntegerField()
    deportes = models.CharField(max_length=2, choices=DEPOR)
    vivienda = models.CharField(max_length=2, choices=VIVIENDA)
    

    def __str__(self):
        return self.personalidad
