# -*- coding: utf-8 -*-

import math

class Punt:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, valor):
        self._x = valor

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, valor):
        self._y = valor
    
    def distancia(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
       
class Poligon:
    maxim = 1000
    def __init__(self):
        self._vertexs = []
        self._superior_esquerra = Punt(Poligon.maxim, Poligon.maxim)
        self._inferior_dreta = Punt()

    @property
    def superior_esquerra(self):
        return self._superior_esquerra

    @property
    def inferior_dreta(self):
        return self._inferior_dreta
    
    def afegeix_vertex(self, pt):
        self._vertexs.append(pt)
        if pt.x < self.superior_esquerra.x:
            self.superior_esquerra.x = pt.x
        else:
            if pt.x > self.inferior_dreta.x:
                self.inferior_dreta.x = pt.x
        if pt.y < self.superior_esquerra.y:
            self.superior_esquerra.y = pt.y
        else:
            if pt.y > self.inferior_dreta.y:
                self.inferior_dreta.y = pt.y
                
    def calcula_perimetre(self):
        perimetre = 0
        for index in range(len(self._vertexs) - 1):
            perimetre += self._vertexs[index].distancia(self._vertexs[index+1])
        perimetre += self._vertexs[0].distancia(self._vertexs[-1])
        return perimetre
    
def test_poligon(llista_punts):
    pol = Poligon()
    for p in llista_punts:
        pt = Punt(p[0], p[1])
        pol.afegeix_vertex(pt)
    sup_esq = pol.superior_esquerra
    inf_dreta = pol.inferior_dreta
    return [pol.calcula_perimetre(), (sup_esq.x, sup_esq.y), (inf_dreta.x, inf_dreta.y)]


resultat = test_poligon([(0,0), (0,1), (1,1), (1,0)])
print(resultat)