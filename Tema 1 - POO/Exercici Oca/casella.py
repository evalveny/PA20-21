# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:32:36 2019

@author: ernest
"""

class Casella:
    CASELLA_NORMAL = 'N'
    CASELLA_OCA = 'O'
    CASELLA_POU = 'P'
    CASELLA_MORT = 'M'
    CASELLA_FINAL = 'F'
    CASELLA_INICIAL = 1
    def __init__(self, posicio = 0, tipus = 'N'):
        self._posicio = posicio
    
    def executa_accio(self, jugador):
        jugador.posicio = self._posicio
        es_oca = False
        return es_oca
               
    @property
    def posicio(self):
        return self._posicio
    
    @posicio.setter
    def posicio(self, posicio):
        self._posicio = posicio
       
    def es_oca(self):
        return False


class Oca(Casella):
    def __init__(self, posicio = 0, tipus = 'O'):
        super().__init__(posicio, tipus)
        
    def executa_accio(self, jugador):
        es_oca = super().executa_accio(jugador)
        es_oca = True
        return es_oca
    
    def es_oca(self):
        return True
    
class Pou(Casella):
    N_TORNS_POU = 2
    def __init__(self, posicio = 0, tipus = 'P'):
        super().__init__(posicio, tipus)
        
    def executa_accio(self, jugador):
        es_oca = super().executa_accio(jugador)
        jugador.torns_inactiu = Pou.N_TORNS_POU
        return es_oca
    
class Mort(Casella):
    def __init__(self, posicio = 0, tipus = 'M'):
        super().__init__(posicio, tipus)
        
    def executa_accio(self, jugador):
        es_oca = super().executa_accio(jugador)
        jugador.posicio = Casella.CASELLA_INICIAL
        return es_oca

class Final(Casella):
    def __init__(self, posicio = 0, tipus = 'F'):
        super().__init__(posicio, tipus)
        
    def executa_accio(self, jugador):
        es_oca = super().executa_accio(jugador)
        jugador.guanya()
        return es_oca
