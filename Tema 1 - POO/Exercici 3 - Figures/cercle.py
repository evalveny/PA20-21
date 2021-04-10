import numpy as np
from punt import Point
from figura import Figura

class Cercle(Figura):
    def __init__(self):
        self._centre = Point(0.0, 0.0)
        self._radi = 0.0

    def area(self):
        return np.pi*self._radi**2

    def perimetre(self):
        return 2*np.pi*self._radi
        
    def llegeix(self):
        print ("Coordenades del centre: ")
        x = float(input("x: "))
        y = float(input("y: "))
        self._centre = Point(x,y)
        self._radi = float(input("Radi: "))
    
    def __str__(self):
        resultat = "Centre: " + str(self._centre) + "\n"
        resultat += "Radi: " + str(self._radi) + "\n"
        return resultat
