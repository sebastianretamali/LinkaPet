from django.shortcuts import render, redirect
from .models import Cuestionario
from .forms import CuestionarioForm


def list_cuestionario(request):
    cuestionario = Cuestionario.objects.all()
    return render(request, 'cuestionario.html', {'cuestionario': cuestionario})

def create_cuestionario(request):
    form = CuestionarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
         form.save()
         return redirect('list_cuestionario')

    return render(request, 'cuestionario.html', {'form': form})




