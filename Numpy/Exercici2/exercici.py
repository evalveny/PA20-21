# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:24:17 2018

@author: ernest
"""

import copy
import numpy as np

def canviaValorForaRang(matriu, n, m, x):
    resultat = copy.deepcopy(matriu)
    resultat[resultat < n] = x
    resultat[resultat > m] = x
    return resultat

def sumaNoDiagonal(matriu):
    dim = matriu.shape[0]
    noDiagonal = np.ones(matriu.shape)
    noDiagonal[np.arange(dim), np.arange(dim)] = 0
    return (matriu * noDiagonal).sum()

def diagonalDominant(matriu):
    dim = matriu.shape[0]
    diagonal = matriu[np.arange(dim), np.arange(dim)]
    maxFila = matriu.max(1)
    return (diagonal == maxFila).all()

def maxFila(matriu):
    maxF = list(matriu.max(1))
    indexMaxF = list(matriu.argmax(1))
    return list((zip(maxF, indexMaxF)))

def intercanviFiles(matriu, i, j):
    resultat = copy.deepcopy(matriu)
    resultat[i,:] = matriu[j,:]
    resultat[j,:] = matriu[i,:]
    return resultat
    

    