# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:53:21 2019

@author: ernest
"""

class Usuari:
    def __init__(self, codi = "", nom = "", edat = 18):
        assert (edat >= 18)
        self._codi = codi
        self._nom = nom
        self._edat = edat
    
    @property
    def codi(self):
        return self._codi
    @codi.setter
    def codi(self, valor):
        self._codi = valor
        
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, valor):
        self._nom = valor
        
    @property
    def edat(self):
        return self._edat
    @edat.setter
    def edat(self, valor):
        assert (valor >= 18)
        self._edat = valor