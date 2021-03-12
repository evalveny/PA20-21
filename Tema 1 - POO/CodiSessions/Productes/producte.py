# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:05:43 2019

@author: Ernestl
"""


            
class Producte:
    def __init__(self, codi = "", preu = 0.0):
        self._codi = codi
        self._preu = preu
        
    @property
    def codi(self):
        return self._codi
    @codi.setter
    def codi(self, valor):
        self._codi = valor
        
    @property
    def preu(self):
        return self._preu
    @preu.setter
    def preu(self, valor):
        self._preu = valor

    def llegeix(self):
        self.codi = input("Codi: ")
        self.preu = float(input("Preu: "))

class Llibre(Producte):
    def __init__(self, codi = "", preu = 0.0, titol = "", autor = "", n_pagines = 0):
        super().__init__(codi, preu)
        self._titol = titol
        self._autor = autor
        self._n_pagines = n_pagines
        self._valoracions = []
    
    @property
    def titol(self):
        return self._titol
    @titol.setter
    def titol(self, valor):
        self._titol = valor

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def n_pagines(self):
        return self._n_pagines
    @n_pagines.setter
    def n_pagines(self, valor):
        self._n_pagines = valor
        
    def llegeix(self):
        super().llegeix()
        self.titol = input("Titol: ")
        self.autor = input("Autor: ")
        self.n_pagines = int(input("N. Pagines: "))

    def afegeix_valoracio(self, puntuacio, missatge):
        self._valoracions.append((puntuacio, missatge))
        
    def despeses_enviament(self):
        despeses = super().despeses_enviament()
        if (self.n_pagines > 500):
            despeses += 1.0
        return despeses

class Electrodomestic(Producte):
    def __init__(self, codi = "", preu = 0.0, marca = "", model = "", volum = 0.0):
        super().__init__(codi, preu)
        self._marca = marca
        self._model = model
        self._volum = volum
        self._distribuidors = []
          
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, valor):
        self._model = valor

    @property
    def volum(self):
        return self._volum
    @volum.setter
    def volum(self, valor):
        self._volum = valor

    def afegeix_distribuidor(self, nom):
        self._distribuidors.append(nom)
        
    def llegeix(self):
        super().llegeix()
        self.marca = input("Marca: ")
        self.model = input("Model: ")
        self.volum = float(input("Volum: "))

    def mostra(self):
        super().mostra()
        print ("Marca: ", self.marca)
        print ("Model: ", self.model)
        print ("Volums: ", self.volum)
        
    def despeses_enviament(self):
        despeses = super().despeses_enviament()
        despeses += int(self.volum / 20)
        return despeses


def llegeix_productes(nom_fitxer):
    llibres = []
    electrodomestics = []
    with open(nom_fitxer) as f:
        for linia in f:
            valors = linia.split()
            if valors[0] == 'L':
                llibre = Llibre(valors[1], float(valors[2]), valors[3], valors[4], int(valors[5]))
                llibres.append(llibre)
            elif valors[0] == 'E':
                elect = Electrodomestic(valors[1], float(valors[2]), valors[3], valors[4], int(valors[5]))
                electrodomestics.append(elect) 
    return llibres, electrodomestics
        
        