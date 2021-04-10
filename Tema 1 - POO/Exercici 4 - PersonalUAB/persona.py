# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:23:53 2019

@author: ernest
"""

class Persona:
    def __init__(self, niu = "", nom = ""):
        self._nom = nom
        self._niu = niu
        self._assignatures = []
    
    @property
    def nom(self):
        return self._nom

    @property
    def niu(self):
        return self._niu
    
    def cercaAssignatura(self, nom):
        return nom in [a.nom for a in self._assignatures]

    def afegeixAssignatura(self, assignatura):
        if not self.cercaAssignatura(assignatura.nom):
            self._assignatures.append(assignatura)
            return True
        else:
            return False
        