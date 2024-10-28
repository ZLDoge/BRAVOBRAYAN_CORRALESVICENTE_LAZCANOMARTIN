from django.shortcuts import render, redirect
from .forms import archivoform, Intento1Form
# Create your views here.

def home(request):
    return render(request, 'home.html')

def form_archivo(request):
    success_message = None  # Variable para el mensaje de éxito
    
    if request.method == 'POST':
        form = Intento1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Archivo y correo subidos correctamente."  # Mensaje de éxito
            return redirect('prueba')
        else:
            # Esto asegura que incluso si el formulario no es válido, devuelva una respuesta
            return render(request, 'form_archivo.html', {'form': form})
    else:
        form = Intento1Form()  # Mostrar formulario vacío si la solicitud es GET
    
    # Siempre se devuelve una respuesta, ya sea para GET o POST
    return render(request, 'form_archivo.html', {'form': form, 'success_message': success_message})



def prueba(request):
    return render(request, 'prueba.html')

def intento(request):
    return render(request, 'intento.html')