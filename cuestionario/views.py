from django.shortcuts import render, redirect
#from .models import Cuestionario
from .forms import CuestionarioForm
from mascota.models  import Mascota
from mascota.views  import  filtro_prueba
from django.contrib.auth.models import User

#Guardar Datos Cuestionario
def create_cuestionario(request):
    form = CuestionarioForm()

    if request.method == "POST":
        form = CuestionarioForm(request.POST)
        
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('list_cuestionario')#'list_cuestionario'

    return render(request, 'cuestionario.html', {'form': form})

#
def list_cuestionario(request):
    if request.method == 'POST':
       form = CuestionarioForm(request.POST, instance=request.cuestionario)

    mascota = filtro_prueba()   

    return render(request, 'aceptar_cuestionario.html', {'mascota': mascota})


def cuestion():
    
    mascota = filtro_prueba()

    return mascota


def update(request, id):
    cuestionario = Cuestionario.objects.get(id=id)
    form = CuestionarioForm(request.POST or None, request.FILES or None, instance=cuestionario)

    if form.is_valid():
        mascota = cuestion() 
        return redirect('list_cuestionario')

    return render(request, 'mascota_form.html', {'form': form, 'cuestionario': cuestionario})


