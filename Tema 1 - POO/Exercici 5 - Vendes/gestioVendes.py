# -*- coding: utf-8 -*-

from producte import Llibre, Electrodomestic
from venda import VendaPresencial, VendaOnline

class GestioVendes():
    def __init__(self):
        self._productes = {}
        self._vendes = []
    
    def llegeixProductes(self, nomFitxer):
        with open(nomFitxer, "rt") as fitxer:
            tipus = fitxer.readline()
            while (tipus != ''):
                codi = fitxer.readline().strip('\n')
                preu = float(fitxer.readline().strip('\n'))
                if int(tipus) == 0:
                    titol = fitxer.readline().strip('\n')
                    autor = fitxer.readline().strip('\n')
                    nPagines = int(fitxer.readline().strip('\n'))
                    llibre = Llibre(codi, preu, titol, autor, nPagines)
                    self._productes[codi] = llibre
                else:
                    marca = fitxer.readline().strip('\n')
                    model = fitxer.readline().strip('\n')
                    volum = float(fitxer.readline().strip('\n'))
                    elect = Electrodomestic(codi, preu, marca, model, volum)
                    self._productes[codi] = elect
                tipus = fitxer.readline()
                
                    
    def afegeixVendaPresencial(self, codiProducte, nUnitats, data, botiga):
        if codiProducte in self._productes:
            venda = VendaPresencial(self._productes[codiProducte], nUnitats, data, botiga)
            self._vendes.append(venda)
            return venda.importTotal()
        else:
            return -1.0

    def afegeixVendaOnline(self, codiProducte, nUnitats, data, adreca):
        if codiProducte in self._productes:
            venda = VendaOnline(self._productes[codiProducte], nUnitats, data, adreca)
            self._vendes.append(venda)
            return venda.importTotal()
        else:
            return -1.0
    
    def escriuVendes(self, nomFitxer):
        with open(nomFitxer, "wt") as fitxer:
            for v in self._vendes:
                v.escriu(fitxer)
    
        