from django.db import models

# Create your models here.

class archivo(models.Model):
    email = models.EmailField()  # Campo de correo electrónico
    uploaded_file = models.FileField(upload_to='uploads/')  # Campo para subir el archivo

    def __str__(self):
        return self.email