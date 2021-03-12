# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:34:45 2021

@author: 1002245
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