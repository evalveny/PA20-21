# -*- coding: utf-8 -*-

class Assignatura:
    def __init__(self, nom = "", nCreditsEstudiant = 0, nCreditsProfessor = 0):
        self._nom = nom
        self._nCreditsEstudiant = nCreditsEstudiant
        self._nCreditsProfessor = nCreditsProfessor
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def creditsEstudiant(self):
        return self._nCreditsEstudiant

    @property
    def creditsProfessor(self):
        return self._nCreditsProfessor
    