# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:34:17 2021

@author: 1002245
"""
import tauler

def joc_oca(nom_fitxer, n_jugadors, valors_dau):
    t = tauler.Tauler()
    t.inicialitza(nom_fitxer, n_jugadors)
    torn = 0
    guanyador = -1
    llista_resultat = []   
    while guanyador == -1 and torn < len(valors_dau):
        repeteix, resultat = t.torn_joc(valors_dau[torn])
        llista_resultat.append(resultat)
        torn += 1
        guanyador = t.guanyador()
        if not repeteix:
            t.canvia_torn()
    return guanyador, llista_resultat
        