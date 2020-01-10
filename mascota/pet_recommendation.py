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
pet_ids = [20, 10, 5, 4]
candidates = set()

# This for-loop is only an example of a concurrent search.
for pet_id in pet_ids:

    ranking, distance = make_recommendation(model_knn=model_knn, data=w_data, fav_dog_id=pet_id, n_recommendations=5)
    
    # Take the first recommendation in the ranking and check if it is in the list

    pet = None

    while ranking and pet not in candidates:
        pet = ranking[0]
        del ranking[0]
        candidates.add(pet)

    if not ranking:
        print('No more candidates')
        pet = np.random.randint(w_data.shape[0])
    
    print(pet_id, pet)
    print(nmf_data.loc[pet])
    print()

