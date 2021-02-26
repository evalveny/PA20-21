# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:58:45 2021

@author: 1002245
"""

class Fitxa:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def valor_compatible(self, valor):
        return valor == self.valor1 or valor == self.valor2
    
    def valor_contrari(self, valor):
        if (self.valor1 == valor):
            return self.valor2
        else:
            return self.valor1
    
class Jugador:
    def __init__(self):
        self.fitxes = []
    
    def afegeix_fitxa(self, fitxa):
        self.fitxes.append(fitxa)
    
    def n_fitxes(self):
        return len(self.fitxes)
    
    def selecciona_fitxa(self, valor_esquerra, valor_dret):
        if (valor_esquerra == -1) and (valor_dret == -1):
            fitxa = self.fitxes[0]
            self.fitxes.pop(0)
        else:
            trobat = False
            i = 0
            while not trobat and i < len(self.fitxes):
                if self.fitxes[i].valor_compatible(valor_esquerra) or \
                    self.fitxes[i].valor_compatible(valor_dret):
                    trobat = True
                    fitxa = self.fitxes[i]
                else:
                    i += 1
            if not trobat:
                fitxa = Fitxa(-1, -1)
            else:
                self.fitxes.pop(i)
        return fitxa
        
class Partida:
    def __init__(self):
        self.jugadors = []
        for i in range(4):
            self.jugadors.append(Jugador())
        self.extrem_esquerra = -1
        self.extrem_dret = -1
        self.jugador_actual = 0
    
    def inicialitza(self, fitxes):
        i = 0
        for jugador in self.jugadors:
            for j in range(7):
                jugador.afegeix_fitxa(fitxes[i])
                i += 1
    
    def juga_torn(self):
        fitxa = self.jugadors[self.jugador_actual].selecciona_fitxa(self.extrem_esquerra, self.extrem_dret)
        if self.extrem_esquerra == -1:
            self.extrem_esquerra = fitxa.valor1
            self.extrem_dret = fitxa.valor2
        else:
            if (fitxa.valor1 != -1):
                if fitxa.valor_compatible(self.extrem_esquerra):
                    self.extrem_esquerra = fitxa.valor_contrari(self.extrem_esquerra)
                else:
                    self.extrem_dret = fitxa.valor_contrari(self.extrem_dret)
        return fitxa
    
    def canvia_torn(self):
        self.jugador_actual = (self.jugador_actual + 1) % 4
    
    def guanyador(self):
        if self.jugadors[self.jugador_actual].n_fitxes() == 0:
            return self.jugador_actual + 1
        else:
            return 0
                
        

def juga_domino(fitxes_inicials):
    joc = Partida()
    joc.inicialitza(fitxes_inicials)
    fitxes_jugades = []
    guanyador = 0
    n_torns_bloquejat = 0
    while n_torns_bloquejat < 4 and guanyador == 0:
        fitxa = joc.juga_torn()
        print(fitxa.valor1, fitxa.valor2)
        fitxes_jugades.append(fitxa)
        if (fitxa.valor1 == -1):
            n_torns_bloquejat += 1
        else:
            n_torns_bloquejat = 0
            guanyador = joc.guanyador()
        joc.canvia_torn()
    return guanyador, fitxes_jugades

fitxes_inicials = []
for i in range(7):
    for j in range(i,7):
        fitxes_inicials.append(Fitxa(i, j))
        
guanyador, fitxes_jugades = juga_domino(fitxes_inicials)