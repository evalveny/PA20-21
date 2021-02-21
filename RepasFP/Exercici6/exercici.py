# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:24:17 2018

@author: ernest
"""


def index_paraules(nomFitxer):
    indexParaules = dict()
    fitxer = open(nomFitxer, "rt")
    for nLinia,textLinia in enumerate(fitxer):
        for caracter in ',.:;!?':
            textLinia = textLinia.replace(caracter, ' ')
        textLinia = textLinia.lower()

        paraules = textLinia.split()
        for paraula in paraules:
            if paraula in indexParaules:
                valor = indexParaules[paraula]
                if valor[-1][0] == nLinia:
                    valor[-1][1] = valor[-1][1] + 1
                else:
                    valor.append([nLinia, 1])
            else:
                valor = [[nLinia, 1]]
            indexParaules[paraula] = valor
    return indexParaules
             


def cerca_paraula(paraula, index, nomFitxer):
    resultat = []
    if paraula in index:
        fitxer = open(nomFitxer, "rt")
        linies = fitxer.readlines()
        valor = index[paraula]
        for linia in valor:
            resultat.append ([linies[linia[0]], linia[1]])
    return resultat
            
            
