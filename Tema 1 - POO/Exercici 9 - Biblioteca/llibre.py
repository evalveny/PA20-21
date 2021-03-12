# -*- coding: utf-8 -*-

from publicacio import Publicacio
import datetime as dt

class Llibre(Publicacio):
    def __init__(self, codi = "", titol = "", autor = "", nCopies = 0, nDiesPrestec = 0):
        super().__init__()
        self._autor = autor
        self._nCopies = nCopies
        self._nDiesPrestec = dt.timedelta(nDiesPrestec)
        self._nPrestecs = 0

    @property
    def autor(self):
        return self._autor
    
    @property
    def nCopies(self):
        return self._nCopies
    
    @property
    def nDiesPrestec(self):
        return self._nDiesPrestec
    
    def presta(self, data, nExemplar = 0):
        correcte = False
        dataRetorn = data
        if self._nPrestecs < self._nCopies:
            correcte = True
            dataRetorn = data + self._nDiesPrestec
            self._nPrestecs += 1
        return correcte, dataRetorn
    
    def retorna(self, nExemplar = 0):
        correcte = False
        if (self._nPrestecs > 0):
            correcte = True
            self._nPrestecs -= 1
        return correcte
            