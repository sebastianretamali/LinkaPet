from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm, ContactForm

from cuestionario.forms import CuestionarioForm
from cuestionario.models import Cuestionario

from django.contrib.auth.models import User

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm

mascota = Mascota.objects.all()
ids_mascotas = []


#listar mascota
def list_mascota(request):
    
    mascota = Mascota.objects.all()

    return render(request, 'mascota.html', {'mascota': mascota})

#crear mascota
def create_mascota(request):
    form = MascotaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
         form.save()
         return redirect('list_mascota')

    return render(request, 'mascota_form.html', {'form': form})

#modificar Mascota
def update_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    form = MascotaForm(request.POST or None, request.FILES or None, instance=mascota)

    if form.is_valid():
         form.save()
         return redirect('list_mascota')

    return render(request, 'mascota_form.html', {'form': form, 'mascota': mascota})

#eliminar mascota
def delete_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        mascota.delete()
        return redirect('list_mascota')

    return render(request, 'masc_delete_confirm.html', {'mascota': mascota})

#descripción mascota match
def descripcion_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    form = MascotaForm(request.POST or None, request.FILES or None, instance=mascota)
    
    if form.is_valid():
         form.save()
         return redirect('list_mascota')

    return render(request, 'mascota_desc.html', {'form': form, 'mascota': mascota})

count_click = 0

#Mostrar mascotas en aleatorio
def aleatorio(request, id): 
    global count_click

    try:
        #if id != 43:
        ranking = test(id)
        mascota = None
        if len(ranking) > count_click:
            mascota = Mascota.objects.filter(id=ranking[count_click])
            count_click = count_click + 1
        else:
            count_click == 0 
            mascota = Mascota.objects.order_by('?')[0],
         
        if  len(mascota) == 0:
            mascota = Mascota.objects.order_by('?')[0],
        #else:

             #return redirect('create_cuestionario')
    except IndexError as error:
        print('error')  
        return redirect('create_cuestionario')
    except UnboundLocalError as error:
        return redirect('create_cuestionario')

    return render(request, 'aceptar_cuestionario.html', {'mascota': mascota})


def filtro_prueba():

    mascota = Mascota.objects.order_by('?')[0],

    return mascota

#Envío de email a fundación
def match_mascota(request, id):
    mascota = Mascota.objects.get(id=id)  
    # varibles para texto mascota elegida
    texto = 'Nombre:', mascota.nombre
    texto += 'Edad:',  mascota.edad 
    texto += 'Sexo:', mascota.sexo 
    texto += 'Tipo:', mascota.tipo 

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = str(texto) + '\n' +  " Mensaje: " + '\n' + message 
            try:
                send_mail(subject, message, from_email, [mascota.mail_fundacion] )
            except BadHeaderError:
                return HttpResponse('Encabezado encontrado no válido.')
            return redirect('success')
    return render(request, "email.html", {'form': form, 'mascota': mascota})



def successView(request):
    html = """<html>
           <body>
           <div class="alert alert-success alert-dismissable">
           <button type="button" class="close" data-dismiss="alert">&times;</button></a>
           <strong>¡Su mensaje a sido envíado con éxito!</strong> .
           </div>
           </body></html>"""
           
    #return render(request, "home.html", HttpResponse(html))
    return redirect('home')
#--------------------------------------------------------------------------------------------------------------------------------------------


    #!/usr/bin/env python
# coding: utf-8

"""
This script implements a simple prototype of pet recommendation using a Nearest Neighbor-base strategy.
A user selects a pet and the algorithm returns the most similar pet from the dataset. The search is 
unsupervised. The algorithm keeps a list of the visited candidates. It recommend a random pet if all the 
candidates are in the list of visited pets.

"""

import os
import pandas as pd
import numpy as np
from joblib import load
from sklearn.neighbors import NearestNeighbors

def test(id):
    print('id', id)
    def make_recommendation(model_knn, data, fav_dog_id, n_recommendations):
        """
        This method makes recommendation based on a nearest neighbor model. Search is unsupervised.
        In every search the algorithm removes the input index because is the most similar instance 
        within the dataset.

        :param model_knn: a Nearest Neighbor class instances previously created.
        :param data: a numpy-array with the dataset transformed by NMF.
        :param fav_dog_id: an int number with the index of the selected dog.
        :param n_recommendations: an int with the number of recommendations returned by the method.

        :returns
            indices: a list with indices of candidates sort ascending in distance.
            distances: a list with the distances between the pet and its neighbors. 

        """

        # Fit the KNN model to the data.
        model_knn.fit(data)

        # Select a query instance
        fav_dog = data[fav_dog_id][np.newaxis, :]
        
        distances, indices = model_knn.kneighbors(fav_dog, n_neighbors=n_recommendations+1)
        r_idx = np.argsort(distances.squeeze()).tolist()
        indices = indices.squeeze()[r_idx].tolist()
        distances = distances.squeeze()[r_idx].tolist()

        d_index = indices.index(fav_dog_id)
        del indices[d_index]
        del distances[d_index]
        return indices, distances

    # Load data from NMF transformation

    nmf_data = load('nmf_coeff.joblib')
    
    w_data = nmf_data[[0, 1]].values

    # Create a instance of Nearest Neighbor model.
    model_knn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree', metric='euclidean')

    # List of selection
    pet_ids = [id]
    #pet_ids = [20, 10, 5, 4]
    candidates = set()

    # This for-loop is only an example of a concurrent search.
    for pet_id in pet_ids:

        ranking, distance = make_recommendation(model_knn=model_knn, data=w_data, fav_dog_id=pet_id, n_recommendations=5)
        
        # Take the first recommendation in the ranking and check if it is in the list
        print('ranking', ranking)
        pet = None

        while ranking and pet not in candidates:
            pet = ranking[0]
            del ranking[0]
            candidates.add(pet)

        if not ranking:
            print('No more candidates')
            pet = np.random.randint(w_data.shape[0])
        
        #print("ids",{pet_id, pet})
        #print("nmf_data",nmf_data.loc[pet])
        #print('candidates', candidates)
        return ranking
       
