# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:51:17 2019

@author: Ernest
"""

import casella as c
import jugador as j

class Tauler():
    def __init__(self):
        self._caselles = []
        self._jugadors = []
        self._jugador_actual = 0
    
    def inicialitza(self, nom_fitxer, nJugadors):
        with open(nom_fitxer) as fitxer:
            for linia in fitxer:
                valors = linia.split()
                posicio = int(valors[0])
                tipus = valors[1]
                if tipus == c.Casella.CASELLA_NORMAL:    
                    nova_casella = c.Casella(posicio)
                elif tipus == c.Casella.CASELLA_FINAL:
                    nova_casella = c.Final(posicio)
                elif tipus == c.Casella.CASELLA_MORT:
                    nova_casella = c.Mort(posicio)
                elif tipus == c.Casella.CASELLA_OCA:
                    nova_casella = c.Oca(posicio)
                else:
                    nova_casella = c.Pou(posicio)
                       
                self._caselles.append(nova_casella)
        for i in range(nJugadors):
            self._jugadors.append(j.Jugador())
        self._jugador_actual = 0
              
    def torn_joc(self, valor_dau):
        jugador_torn = self._jugadors[self._jugador_actual]
        repeteix_torn = False
        pot_tirar = False
        if jugador_torn.pot_tirar():
            pot_tirar = True
            nova_posicio = jugador_torn.posicio + valor_dau
            if nova_posicio <= len(self._caselles):
                es_oca = self._caselles[nova_posicio-1].executa_accio(jugador_torn)
                if es_oca:
                    try:
                        posicio_oca = [c.posicio for c in self._caselles[nova_posicio:] if c.es_oca()]
                        jugador_torn.posicio = posicio_oca[0]
                        repeteix_torn = True
                    except:
                        pass
            else:
                nova_posicio = -1
        else:
            jugador_torn.passa_torn()
        return repeteix_torn, (self._jugador_actual + 1, pot_tirar, jugador_torn.posicio)
    
    def guanyador(self):
        if self._jugadors[self._jugador_actual].es_guanyador():
            return self._jugador_actual + 1
        else:
            return -1
    
    def canvia_torn(self):
        self._jugador_actual = (self._jugador_actual + 1) % len(self._jugadors)

        
        
                
                    
        
