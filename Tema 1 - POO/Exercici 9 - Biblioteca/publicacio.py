# -*- coding: utf-8 -*-

import abc

class Publicacio(metaclass = abc.ABCMeta):
    def __init__(self, codi = "", titol = ""):
        self._codi = codi
        self._titol = titol
    
    @property
    def codi(self):
        return self._codi
    
    @property
    def titol(self):
        return self._titol
    
    @abc.abstractmethod
    def presta(self, data, nExemplar = 0):
        raise NotImplementedError()
        
    @abc.abstractmethod
    def retorna(self, nExemplar = 0):
        raise NotImplementedError()


        
