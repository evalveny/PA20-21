# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:20:09 2019

@author: ernest
"""

class Jugador:
    def __init__(self, casella = 1, n_torns_inactiu = 0, guanyador = False):
        self._casella = casella
        self._n_torns_inactiu = n_torns_inactiu
        self._guanyador = guanyador
    
    @property
    def posicio(self):
        return self._casella
    
    @posicio.setter
    def posicio(self, casella):
        self._casella = casella
    
    @property
    def torns_inactiu(self):
        return self._n_torns_inactiu
    
    @torns_inactiu.setter
    def torns_inactiu(self, n_torns):
        self._n_torns_inactiu = n_torns
 
    def passa_torn(self):
        if self._n_torns_inactiu > 0:
            self._n_torns_inactiu -= 1
    
    def pot_tirar(self):
        return self._n_torns_inactiu == 0
    
    def guanya(self):
        self._guanyador = True
    
    def es_guanyador(self):
        return self._guanyador