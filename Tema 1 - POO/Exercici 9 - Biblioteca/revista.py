# -*- coding: utf-8 -*-

from publicacio import Publicacio
import datetime as dt

class Revista(Publicacio):
    diesPrestec = dt.timedelta(30)
    def __init__(self, codi = "", titol = "", periodicitat = ""):
        super().__init__(codi, titol)
        self._periodicitat = periodicitat
        self._exemplars = {}
        
    @property
    def periodicitat(self):
        return self._periodicitat
    
    def afegeixExemplar(self, nExemplar):
        self._exemplars[nExemplar] = False
    
    def presta(self, data, nExemplar):
        correcte = False
        dataRetorn = data
        if nExemplar in self._exemplars:
            if not self._exemplars[nExemplar]:
                self._exemplars[nExemplar] = True
                dataRetorn = data + Revista.diesPrestec
                correcte = True
        return correcte, dataRetorn
    
    def retorna(self, nExemplar):
        correcte = False
        if nExemplar in self._exemplars:
            if self._exemplars[nExemplar]:
                self._exemplars[nExemplar] = False
                correcte = True
        return correcte