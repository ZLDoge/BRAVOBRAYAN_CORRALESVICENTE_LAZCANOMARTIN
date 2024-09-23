# core/urls.py

from django.urls import path
from .views import home, form_archivo

urlpatterns = [
    path('',home, name='home'),  # Ruta principal que apunta a la vista home
    path('form-archivo', form_archivo, name='form_archivo'),
]

