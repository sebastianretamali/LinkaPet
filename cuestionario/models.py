from django.db import models
from mascota.models import Mascota
from django.contrib.auth.models import User

#Choices personalidad
PERSO = (
        ('ME', 'Muy extrovertido'),
        ('E', 'Extrovertido'),
        ('N', 'Neutral'),
        ('I', 'Introvertido'),
        ('MI', 'Muy introvertido'),
    )

#Choices cantidad de niños
NINOS = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'Más de 5'),
    )

#Choices deporte
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

#Choices vivienda
VIVIENDA = (
        ('C', 'Casa con patio'),
        ('DC', 'Dpto Chico o Mediano'),
        ('DG', 'Dpto Grande'),
        ('P', 'Parcela'),
    )

#Clase Cuestionario
class Cuestionario(models.Model):
      personalidad = models.CharField(max_length=2, choices=PERSO)
      cant_ninos = models.CharField(max_length=1, choices=NINOS)
      edad = models.IntegerField()
      deportes = models.CharField(max_length=2, choices=DEPOR)
      vivienda = models.CharField(max_length=2, choices=VIVIENDA)
      usuario = models.ForeignKey(User, null=True,  blank=True,  on_delete=models.CASCADE)
      
      #getter  personalidad
      def __str__(self):
        return self.personalidad

      #getter  cant_ninos
      def __str__(self):
        return self.cant_ninos
      
      #getter  edad
      def __str__(self):
        return self.edad
  
      #getter  deportes
      def __str__(self):
        return self.deportes

      #getter  vivienda
      def __str__(self):
        return self.vivienda




