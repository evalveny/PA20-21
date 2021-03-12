# -*- coding: utf-8 -*-

from llibre import Llibre
from revista import Revista
from prestec import Prestec


class Biblioteca:
    def __init__(self):
        self._publicacions = {}
        self._prestecs = []
    
    def llegeixPublicacions(self, nomFitxer):
        with open(nomFitxer) as fitxer:
            tipus = fitxer.readline().strip('\n')
            while (tipus != ''):
                codi = fitxer.readline().strip('\n')
                titol = fitxer.readline().strip('\n')
                if tipus == 'L':
                    autor = fitxer.readline().strip('\n')
                    nCopies = int(fitxer.readline().strip('\n'))
                    nDiesPrestec = int(fitxer.readline().strip('\n'))
                    llibre = Llibre(codi, titol, autor, nCopies, nDiesPrestec)
                    self._publicacions[codi] = llibre
                else:
                    periodicitat = fitxer.readline().strip('\n')
                    revista = Revista(codi, titol, periodicitat)
                    exemplars = fitxer.readline().strip('\n').split()
                    for e in exemplars:
                        revista.afegeixExemplar(int(e))
                    self._publicacions[codi] = revista
                tipus = fitxer.readline().strip('\n')

    def presta(self, codiUsuari, codiPub, dataPrestec, nExemplar):
        correcte = False
        dataRetorn = dataPrestec
        if codiPub in self._publicacions:
            correcte, dataRetorn = self._publicacions[codiPub].presta(dataPrestec, nExemplar)
            if correcte:
                p = Prestec(codiUsuari, codiPub, dataPrestec, dataRetorn, nExemplar)
                self._prestecs.append(p)
        return correcte, dataRetorn
    
    def retorna(self, codiUsuari, codiPublicacio, nExemplar, data):
        correcte = False
        dataCorrecta = False
        prestecs = list(filter(lambda p: p.codiUsuari == codiUsuari and p.codiPublicacio == codiPublicacio and p.nExemplar == nExemplar, self._prestecs))
        if prestecs != []:
            correcte = self._publicacions[codiPublicacio].retorna(nExemplar)
            if correcte:
                if data < prestecs[0].dataRetorn:
                    dataCorrecta = True
                else:
                    dataCorrecta = False
                self._prestecs.remove(prestecs[0])
        return correcte, dataCorrecta
                    
                
            