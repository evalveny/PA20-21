# -*- coding: utf-8 -*-
import math

class Vector:
    def __init__(self, valors):
        self.valors = valors
    
    def __str__(self):
        sortida = "[" + str(self.valors[0])
        for v in self.valors[1:]:
            sortida = sortida + "," + str(v)
        sortida = sortida + "]"
        return sortida
    
    def __add__(self, v):
        if len(self.valors) != len(v.valors):
            raise ValueError
        suma = [v1 + v2 for v1, v2 in zip(self.valors, v.valors)]
        return Vector(suma)
    
    def __sub__(self, v):
        if len(self.valors) != len(v.valors):
            raise ValueError
        distancia = [(v1 - v2)**2 for v1, v2 in zip(self.valors, v.valors)]
        return math.sqrt(sum(distancia))

    def __mul__(self, v):
        if len(self.valors) != len(v.valors):
            raise ValueError
        multiplicacio = sum([v1 * v2 for v1, v2 in zip(self.valors, v.valors)])
        return multiplicacio        

def opera_vectors(llista_vector_1, llista_vector_2, operacio):
    v1 = Vector(llista_vector_1)
    v2 = Vector(llista_vector_2)
    try:
        if operacio == '+':
            resultat = v1 + v2
        elif operacio == '-':
            resultat = v1 - v2
        elif operacio == '*':
            resultat = v1 * v2
    except:
        resultat = None
    return resultat

    