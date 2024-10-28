from django.urls import path 
from .views import home, form_archivo, prueba, intento

urlpatterns = [
    path('', home, name="home"),
    path('form-archivo', form_archivo, name="form_archivo"),
    path('prueba', prueba, name="prueba"),
    path('intento', intento, name="intento"),
]    