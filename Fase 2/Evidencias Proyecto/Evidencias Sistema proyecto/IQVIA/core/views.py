from django.shortcuts import render

# Create your views here.

def  home(request): 

    return render(request, 'core/home.html')

def form_archivo(request):
    return render (request, 'core/form_archivo.html')

from django.shortcuts import render
from .forms import archivoform

def form_archivo(request):
    if request.method == 'POST':
        form = archivoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o mostrar un mensaje de éxito
    else:
        form = archivoform()  # Inicializa el formulario vacío si es GET

    return render(request, 'core/form_archivo.html', {'form': form})
