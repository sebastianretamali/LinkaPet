from django.db import models

#Clase Fundación
class Fundacion(models.Model):
      username = models.CharField(max_length=20)
      password = models.CharField(max_length=20)
      first_name =  models.CharField(max_length=20)
      last_name = models.CharField(max_length=20)
      email = models.CharField(max_length=20)

      def __str__(self):
        return self.username

