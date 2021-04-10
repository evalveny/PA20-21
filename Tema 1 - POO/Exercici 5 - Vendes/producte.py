# -*- coding: utf-8 -*-

class Producte:
    def __init__(self, codi = "", preu = 0.0):
        self._codi = codi
        self._preu = preu
        
    @property
    def codi(self):
        return self._codi
    @codi.setter
    def codi(self, valor):
        self._codi = valor
        
    @property
    def preu(self):
        return self._preu
    @preu.setter
    def preu(self, valor):
        self._preu = valor

    def llegeix(self):
        self.codi = input("Codi: ")
        self.preu = float(input("Preu: "))
        
    def mostra(self):
        print ("Codi: ", self.codi)
        print ("Preu: ", self.preu)
        
    def despesesEnviament(self):
        if (self.preu < 100):
            despeses = 1.0
        else:
            despeses = min(5.0, 0.01 * self.preu)
        return despeses
    
    def descompte(self, nUnitats):
        return 0.0

            

class Llibre(Producte):
    count = 0
    def __init__(self, codi = "", preu = 0.0, titol = "", autor = "", nPagines = 0):
        Llibre.count += 1
        super().__init__(codi, preu)
        self._titol = titol
        self._autor = autor
        self._nPagines = nPagines
    
    @property
    def titol(self):
        return self._titol
    @titol.setter
    def titol(self, valor):
        self._titol = valor

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def nPagines(self):
        return self._nPagines
    @nPagines.setter
    def nPagines(self, valor):
        self._nPagines = valor
        
    def llegeix(self):
        super().llegeix()
        self.titol = input("Titol: ")
        self.autor = input("Autor: ")
        self.nPagines = int(input("N. Pagines: "))

    def mostra(self):
        super().mostra()
        print ("Titol: ", self.titol)
        print ("Autor: ", self.autor)
        print ("N. pagines: ", self.nPagines)
        
    def despesesEnviament(self):
        despeses = super().despesesEnviament()
        if (self.nPagines > 500):
            despeses += 1.0
        return despeses

    def descompte(self, nUnitats):
        if nUnitats > 100:
            return 0.1
        elif nUnitats > 10:
        		return 0.05
        else:
            return 0.0
            
class Electrodomestic(Producte):
    def __init__(self, codi = "", preu = 0.0, marca = "", model = "", volum = 0.0):
        self._codi = codi
        self._preu = preu
        self._marca = marca
        self._model = model
        self._volum = volum
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, valor):
        self._model = valor

    @property
    def volum(self):
        return self._volum
    @volum.setter
    def volum(self, valor):
        self._volum = valor

    def llegeix(self):
        super().llegeix()
        self.marca = input("Marca: ")
        self.model = input("Model: ")
        self.volum = float(input("Volum: "))

    def mostra(self):
        super().mostra()
        print ("Marca: ", self.marca)
        print ("Model: ", self.model)
        print ("Volums: ", self.volum)
        
    def despesesEnviament(self):
        despeses = super().despesesEnviament()
        despeses += int(self.volum / 20) + 1
        return despeses

    def descompte(self, nUnitats):
        if nUnitats > 1:
        		return 0.1
        else:
            return 0.0
                



        
        
        
        