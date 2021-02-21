# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:24:17 2018

@author: ernest
"""


def index_caracter(nomFitxer):
    index = dict()
    fitxer = open(nomFitxer, "rt")
    for linia in fitxer:
        for caracter in ',.:;!?':
            linia = linia.replace(caracter, ' ')
        linia = linia.lower()
        paraules = linia.split()
        for paraula in paraules:
            for caracter in paraula:
                if ((caracter >= 'a') and (caracter <= 'z')):
                    if caracter in index:
                        valor = index[caracter]
                        if (paraula not in valor[1]):
                            valor[0] = valor[0] + 1
                            valor[1].append(paraula)
                    else:
                        valor = [1, [paraula]]
                    index[caracter] = valor
    return index

def max_paraula_caracter(index):
    resultat = []
    for caracter, valor in sorted(index.items()):
        paraules = [paraula for paraula in valor[1]]
        lenParaules = [len(paraula) for paraula in paraules]
        maxLongitud = max(lenParaules)
        maxParaula = paraules[lenParaules.index(maxLongitud)]
        resultat.append([caracter, maxParaula])
    return resultat
        


    
