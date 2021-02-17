# -*- coding: utf-8 -*-

import random

class Codi:
    def __init__(self, n_valors = 4):
        self.codi = []
        self.n_valors = n_valors

    def genera(self, valors_possibles):
        for i in range(n_valors):
            valor = random.randrange(len(valors_possibles))
            codi_secret.append(valors_possibles[valor])
    
    def conte_valor(self, valor):
        return valor in self.codi

class Intent:
    def __init__(self, n_valors):
        self.n_valors = n_valors
        self.combinacio = []
        self.resultat = []

    def llegeix(self, valors_possibles):
        combinacio = list(input("Introdueix la teva combinacio de colors (sense espais): "))
        assert (len(combinacio) == self.n_valors), combinacio
        for valor in combinacio:
            assert (valor in valors_possibles), combinacio
    
    def comprova(self, codi_secret):
        
        resultat = [ ]
        codi_aux = codi_secret.codi[:]
        combinacio_aux = combinacio[:]
        for index, valor in enumerate(combinacio):
            if (valor == codi_aux[index]):
                resultat.append(1)
                codi_aux[index] = ' '
                combinacio_aux[index] = ' '
        for valor in combinacio_aux:
            if (valor != ' '):
                if valor in codi_aux:
                    posicio = codi_aux.index(valor)
                    resultat.append(0)
                    codi_aux[posicio] = ' '
    return resultat

    
def mastermind(n_valors, max_intents, codi_secret, colors_disponibles):
    resultat = []
    llista_combinacions = []
    endevinat = False
    final = False
    n_intents = 0
    print("Codi secret generat")
    print("Els colors vàlids són: ")
    for clau, valor in colors_disponibles.items():
        print(clau, valor)
    while ((not endevinat) and (not final)):
        try:
            combinacio = llegeix_combinacio(n_valors, colors_disponibles)
            llista_combinacions.append(combinacio)            
            resultat_intent = comprova_combinacio(combinacio, codi_secret)
            resultat.append(resultat_intent)
            print ("Comprovació amb el codi secret: ", resultat_intent)
            if (resultat_intent == [1, 1, 1, 1, 1]):
                endevinat = True
            n_intents = n_intents + 1
            if (n_intents == max_intents):
                final = True
        except AssertionError as missatge:
            print("ERROR: ", missatge)
            llista_combinacions.append(str(missatge))
            resultat.append("ERROR")
    if (endevinat):
        print ("Enhorabona. Has guanyat en ", n_intents, "intents")
    else:
        print ("Ho sento. Has perdut. El codi secret era: ", codi_secret)
    return endevinat, llista_combinacions, resultat

