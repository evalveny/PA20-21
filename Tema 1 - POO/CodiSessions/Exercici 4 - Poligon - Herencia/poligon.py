# -*- coding: utf-8 -*-

import math
import punt

class Poligon:
    maxim = 1000
    def __init__(self, vertexs = []):
        if len(vertexs) != 0 and len(vertexs) <= 2:
            raise ValueError
        self._vertexs = vertexs
    
    def afegeix_vertex(self, pt):
        self._vertexs.append(pt)
                
    def perimetre(self):
        perimetre = 0
        for index in range(len(self._vertexs) - 1):
            perimetre += (self._vertexs[index] - self._vertexs[index+1])
        perimetre += (self._vertexs[0] - self._vertexs[-1])
        return perimetre
    
    def area(self):
        raise NotImplementedError('implementat a les subclasses')
    
    def __str__(self):
        resultat = "["
        for v in self._vertexs:
            resultat = resultat + str(v)
        resultat = resultat + "]"
        return resultat

class Triangle(Poligon):
    def __init__(self, vertexs):
        if len(vertexs) != 3:
            raise ValueError
        super().__init__(vertexs)
    
    def afegeix_vertex(self):
        raise Exception('Un triangle nomes pot tenir tres vertexs')
        
    def area(self):
        a = self._vertexs[0] - self._vertexs[1]
        b = self._vertexs[1] - self._vertexs[2]
        c = self._vertexs[2] - self._vertexs[0]
        s = (a + b + c) / 2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

class Quadrat(Poligon):
    def __init__(self, vertexs):
        if len(vertexs) != 4:
            raise ValueError
        self._costat = vertexs[0] - vertexs[-1]
        if self._costat == 0:
            raise ValueError
        for i in range(len(vertexs) - 1):
            if vertexs[i] - vertexs[i+1] != self._costat:
                raise ValueError
        super().__init__(vertexs)
    
    @property
    def costat(self):
        return self._costat
    @costat.setter
    def costat(self, valor):
        self._costat = valor
        
    def afegeix_vertex(self):
        raise Exception('Un quadrat nomes pot tenir 4 vertexs')
        
    def perimetre(self):
        return 4*self._costat

    def area(self):
        return self._costat**2


def llegeix_poligons(nom_fitxer):
    poligons = []
    with open(nom_fitxer) as f:
        for linia in f:
            valors = linia.split()
            tipus = valors[0]
            punts_x = [int(x) for x in valors[1::2]]
            punts_y = [int(y) for y in valors[2::2]]
            vertexs = []
            for x,y in zip(punts_x, punts_y):
                vertexs.append(punt.Punt(x,y))
            if tipus == 'P':
                p = Poligon(vertexs)
            elif tipus == 'T':
                p = Triangle(vertexs)
            elif tipus == 'Q':
                p = Quadrat(vertexs)
            poligons.append(p)
    return poligons

def test_poligon(poligons):
    resultat = []
    for p in poligons:
        try:
            perimetre = p.perimetre()
        except:
            perimetre = -1
        try:
            area = p.area()
        except:
            area = -1
        resultat.append((perimetre, area))
    return resultat
                
        
        
l = llegeix_poligons('dades_poligons.txt')
resultat = test_poligon(l)
        