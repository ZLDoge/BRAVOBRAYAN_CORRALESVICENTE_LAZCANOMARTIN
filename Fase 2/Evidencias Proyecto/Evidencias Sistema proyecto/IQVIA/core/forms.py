from django import forms
from django.forms import ModelForm
from .models import archivo

class archivoform(ModelForm):
    class Meta:  # Cambia 'meta' a 'Meta'
        model= archivo
        fields = ['email', 'uploaded_file']
