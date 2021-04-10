

from punt import Point
from figura import Figura

class Rectangle(Figura):
    def __init__(self):
        self._topLeft = Point(0.0,0.0)
        self._base = 0.0
        self._alcada = 0.0

    def area(self):
        return self._base * self._alcada

    def perimetre(self):
        return 2 * self._base + 2 * self._alcada
        
    def llegeix(self):
        print ("Coordenades de la cantonada superior esquerra: ")
        x = float(input("x: "))
        y = float(input("y: "))
        self._topLeft = Point(x,y)
        self._base = float(input("Base: "))
        self._alcada = float(input("Alçada: "))
    
    def __str__(self):
        resultat = "Origen: " + str(self._topLeft) + "\n" 
        resultat += "Base: " + str(self._base) + "\n" 
        resultat += "Alçada: " + str(self._alcada) + "\n" 
        return resultat

