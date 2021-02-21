# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:43:25 2018

@author: ernest
"""
import random

def afegeix_sinonim(diccionari, paraula, sinonim):
    if paraula in diccionari:
        if sinonim not in diccionari[paraula]:
            diccionari[paraula].append(sinonim)
    else:
        diccionari[paraula] = [sinonim]


def conversio_sinonims(frase, diccionari):
    novaFrase = []
    for paraula in frase:
        if paraula in diccionari.keys():
            sinonims = diccionari[paraula]
            n = random.randrange(len(sinonims))
            novaFrase.append(sinonims[n])
        else:
            novaFrase.append(paraula)
                
    return novaFrase
    
