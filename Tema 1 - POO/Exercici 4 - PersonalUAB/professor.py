# -*- coding: utf-8 -*-

from persona import Persona

class Professor(Persona):
    def __init__(self, niu, nom, departament, maximCredits):
        super().__init__(niu, nom)
        self._departament = departament
        self._maximCredits = maximCredits
    
    @property
    def departament(self):
        return self._departament

    @property
    def maximCredits(self):
        return self._maximCredits
    
    def creditsImpartits(self):
        return sum([a.creditsProfessor for a in self._assignatures])