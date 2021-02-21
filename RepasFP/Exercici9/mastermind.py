# -*- coding: utf-8 -*-

import random

class Codi:
    def __init__(self, n_valors = 4, combinacio = []):
        self.codi = combinacio
        self.n_valors = n_valors

    def genera(self, valors_possibles):
        for i in range(self.n_valors):
            valor = random.randrange(len(valors_possibles))
            self.codi.append(valors_possibles[valor])
    
    def get_valor(self, posicio):
        return self.codi[posicio]
    
    def indexs_valor(self, valor):
        return [i for i, v in enumerate(self.codi) if v == valor]

class Intent:
    def __init__(self, n_valors):
        self.n_valors = n_valors
        self.combinacio = []
        self.resultat = []
        self.correcte = True

    def llegeix(self, valors_possibles):
        self.combinacio = list(input("Introdueix la teva combinacio de colors (sense espais): "))
        if (len(self.combinacio) != self.n_valors):
            self.correcte = False
        else:
            for valor in self.combinacio:
                if valor not in valors_possibles:
                    self.correcte = False
        return not self.correcte
    
    def comprova(self, codi_secret):      
        self.resultat = [ ]
        codi_aux = [0] * self.n_valors
        combinacio_aux = [0] * self.n_valors
        for index, valor in enumerate(self.combinacio):
            if (valor == codi_secret.get_valor(index)):
                self.resultat.append(1)
                codi_aux[index] = 1
                combinacio_aux[index] = 1
        for index, valor in enumerate(self.combinacio):
            if (combinacio_aux[index] == 0):
                indexs = codi_secret.indexs_valor(valor)
                trobat = False
                n_valors = len(indexs)
                i = 0
                while i < n_valors and not trobat:
                    if codi_aux[indexs[i]] == 0:
                        codi_aux[indexs[i]] = 1
                        self.resultat.append(0)
                        combinacio_aux[index] = 1
                        trobat = True
                    i = i + 1 
                        
    
    def get_resultat(self):
        return self.resultat

    def get_combinacio(self):
        return self.combinacio
    
    def get_correcte(self):
        return self.correcte
    
def mastermind(n_valors, max_intents, codi_secret, colors_disponibles):
    llista_combinacions = []
    endevinat = False
    final = False
    n_intents = 0
    print("Codi secret generat")
    print("Els colors vàlids són: ")
    for clau, valor in colors_disponibles.items():
        print(clau, valor)
    while ((not endevinat) and (not final)):
        combinacio = Intent(n_valors)
        error = combinacio.llegeix(colors_disponibles)
        if not error:
            combinacio.comprova(codi_secret)
            llista_combinacions.append(combinacio)            
            print ("Comprovació amb el codi secret: ", combinacio.get_resultat())
            if (combinacio.get_resultat() == [1, 1, 1, 1, 1]):
                endevinat = True
            n_intents = n_intents + 1
            if (n_intents == max_intents):
                final = True
        else:
            print("ERROR: ", combinacio.get_combinacio())
            llista_combinacions.append(combinacio)
    if (endevinat):
        print ("Enhorabona. Has guanyat en ", n_intents, "intents")
    else:
        print ("Ho sento. Has perdut. El codi secret era: ", codi_secret)
    return endevinat, llista_combinacions

