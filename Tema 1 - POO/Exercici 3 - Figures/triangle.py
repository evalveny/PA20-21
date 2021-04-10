

from punt import Point
from figura import Figura

class Triangle(Figura):
    def __init__(self):
        self._vertexs = []

    def area(self):
        a = self._vertexs[0] - self._vertexs[1]
        b = self._vertexs[1] - self._vertexs[2]
        c = self._vertexs[2] - self._vertexs[0]
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5    

    def perimetre(self):
        perimetre = 0
        for index in range(len(self._vertexs) - 1):
            perimetre += (self._vertexs[index] - self._vertexs[index+1])
        perimetre += (self._vertexs[0] - self._vertexs[-1])
        return perimetre
        
    def llegeix(self):
        for i in range(3):
            print ("Coordenades del vertex: ")
            x = float(input("x: "))
            y = float(input("y: "))
            self._vertexs.append(Point(x,y))
    
    def __str__(self):
        resultat = "Vertexs: " + str(self._vertexs[0]) + ", " 
        resultat += str(self._vertexs[1]) + ", " 
        resultat += str(self._vertexs[2]) + "\n"
        return resultat

