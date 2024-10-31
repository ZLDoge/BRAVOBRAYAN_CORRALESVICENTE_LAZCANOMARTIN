from django import forms 
from django.forms import ModelForm
from .models import intento1, bbdd

class archivoform(ModelForm):
    class Meta:
        model = intento1
        fields = ['correo', 'documento']

class Intento1Form(forms.ModelForm):
    class Meta:
        model = bbdd
        fields = ['correo', 'documento1', 'documento2']  