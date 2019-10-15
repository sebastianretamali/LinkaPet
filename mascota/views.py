from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm

def list_mascota(request):
    mascota = Mascota.objects.all()
    return render(request, 'mascota.html', {'mascota': mascota})


def create_mascota(request):
    form = MascotaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
         form.save()
         return redirect('list_mascota')

    return render(request, 'mascota_form.html', {'form': form})

def update_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    form = MascotaForm(request.POST or None, request.FILES or None, instance=mascota)

    if form.is_valid():
         form.save()
         return redirect('list_mascota')

    return render(request, 'mascota_form.html', {'form': form, 'mascota': mascota})


def delete_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        mascota.delete()
        return redirect('list_mascota')

    return render(request, 'masc_delete_confirm.html', {'mascota': mascota})


