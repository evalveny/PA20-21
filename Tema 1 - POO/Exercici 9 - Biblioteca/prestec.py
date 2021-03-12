# -*- coding: utf-8 -*-

import datetime as dt
class Prestec:
    def __init__(self, codiUsuari = "", codiPublicacio = "", dataPrestec = dt.date(1,1,1), dataRetorn = dt.date(1,1,1), nExemplar = 0):
        self._codiUsuari = codiUsuari
        self._codiPublicacio = codiPublicacio
        self._dataPrestec = dataPrestec
        self._dataRetorn = dataRetorn
        self._nExemplar = nExemplar
    
    @property
    def codiUsuari(self):
        return self._codiUsuari

    @property
    def codiPublicacio(self):
        return self._codiPublicacio

    @property
    def dataPrestec(self):
        return self._dataPrestec

    @property
    def dataRetorn(self):
        return self._dataRetorn

    @property
    def nExemplar(self):
        return self._nExemplar
