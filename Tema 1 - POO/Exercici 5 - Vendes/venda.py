# -*- coding: utf-8 -*-

class Venda:
    def __init__(self, producte, nUnitats = 0, data = ""):
        self._producte = producte
        self._nUnitats = nUnitats
        self._data = data
    
    def importTotal(self):
        return self._nUnitats * self._producte.preu
    
    @property
    def nUnitats(self):
        return self._nUnitats
    @nUnitats.setter
    def nUnitats(self, valor):
        self._nUnitats = valor
    
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, valor):
        self._data = valor
    
    def escriu(self, fitxer):
        linies = [self._producte.codi+'\n', str(self.nUnitats)+'\n', self._data+'\n']
        fitxer.writelines(linies)
        
class VendaOnline(Venda):
    def __init__(self, producte, nUnitats = 0, data = "", adrecaEnviament = ""):
        super().__init__(producte, nUnitats, data)
        self._adrecaEnviament = adrecaEnviament
       
    def importTotal(self):
        preu = super().importTotal()
        preu += self._producte.despesesEnviament()
        preu -= preu * self._producte.descompte(self._nUnitats) 
        return preu

    def escriu(self, fitxer):
        super().escriu(fitxer)
        linies = [str(self.importTotal()).rstrip('0').rstrip('.')+'\n', str(self._producte.despesesEnviament()).rstrip('0').rstrip('.')+'\n', self._adrecaEnviament+'\n']
        fitxer.writelines(linies)
        
class VendaPresencial(Venda):
    def __init__(self, producte, nUnitats = 0, data = "", botiga = ""):
        super().__init__(producte, nUnitats, data)
        self._botiga = botiga
       
    def importTotal(self):
        preu = super().importTotal()
        preu -= preu * self._producte.descompte(self._nUnitats)
        return preu

    def escriu(self, fitxer):
        super().escriu(fitxer)
        linies = [str(self.importTotal()).rstrip('0').rstrip('.') + '\n', self._botiga + '\n']
        fitxer.writelines(linies)
        