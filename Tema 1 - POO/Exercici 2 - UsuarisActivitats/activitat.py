# -*- coding: utf-8 -*-

import usuari as u

class Activitat:
    def __init__(self, nom = "", maxim = 0, edatMin = 18, edatMax = 0, dia = "", hora = ""):
        assert (maxim <= 40 and maxim >= 0 and edatMin >= 18)
        self._nom = nom
        self._maxUsuaris = maxim
        self._edatMin = edatMin
        self._edatMax = edatMax
        self._dia = dia
        self._hora = hora
        self._usuaris = []
    
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, valor):
        self._nom = valor
    
    @property
    def maxParticipants(self):
        return self._maxUsuaris
    @maxParticipants.setter
    def maxParticipants(self, valor):
        assert (valor <= 40)
        self._maxUsuaris = valor
    
    @property
    def edatMinima(self):
        return self._edatMin
    @edatMinima.setter
    def edatMinima(self, valor):
        assert (valor >= 18)
        self._edatMin = valor
    
    @property
    def edatMaxima(self):
        return self._edatMax
    @edatMaxima.setter
    def edatMaxima(self, valor):
        self._edatMax = valor

    @property
    def dia(self):
        return self._dia
    @dia.setter
    def dia(self, valor):
        self._dia = valor

    @property
    def hora(self):
        return self._hora
    @hora.setter
    def hora(self, valor):
        self._hora = valor        
    
    def nParticipants(self):
        return len(self._usuaris)

    def buscaParticipant(self, nom):
        participant = [usr for usr in self._usuaris if usr.nom == nom]
        if (participant == []):
            return None
        else:
            return participant[0]
    
    def afegeixParticipant(self, usr):
        assert (usr.edat >= self.edatMinima and usr.edat <= self.edatMaxima), "error edat"
        assert (self.buscaParticipant(usr.nom) == None), "error ja inscrit"
        assert (self.nParticipants() < self.maxParticipants), "error maxim participants"
        self._usuaris.append(usr)
        
