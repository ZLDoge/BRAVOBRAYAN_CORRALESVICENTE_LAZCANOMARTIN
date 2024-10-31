from django.urls import path 
from .views import home, form_archivo, prueba, intento, login_view

urlpatterns = [
    path('', home, name="home"),
    path('form-archivo', form_archivo, name="form_archivo"),
    path('prueba', prueba, name="prueba"),
    path('intento', login_view, name="intento"),# Nueva URL para la página de cálculo

]    