# -*- coding: utf-8 -*-

from persona import Persona

class Estudiant(Persona):
    def __init__(self, niu, nom, titulacio):
        super().__init__(niu, nom)
        self._titulacio = titulacio
    
    @property
    def titulacio(self):
        return self._titulacio
    
    def creditsMatriculats(self):
        return sum([a.creditsEstudiant for a in self._assignatures])