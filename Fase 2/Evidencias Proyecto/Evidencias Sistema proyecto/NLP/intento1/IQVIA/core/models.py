from django.db import models

# Create your models here.

from django.db import models

class intento1(models.Model):
    correo = models.EmailField(max_length=254)  # Campo de correo electrónico
    documento = models.FileField(upload_to='archivos/')


class bbdd(models.Model):
    correo = models.EmailField(max_length=254)  # Campo de correo electrónico
    documento1 = models.FileField(upload_to='archivos/')  # Primer archivo
    documento2 = models.FileField(upload_to='archivos/')  # Segundo archivo

    def __str__(self):
        return self.correo

