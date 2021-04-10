# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:16:58 2019

@author: Ernest
"""

class NombreRacional:
    def __init__(self, numerador = 0, denominador = 0):
        self._numerador = numerador
        self._denominador = denominador
    
    @property
    def numerador(self):
        return self._numerador
    @numerador.setter
    def numerador(self, valor):
        self._numerador = valor

    @property
    def denominador(self):
        return self._denominador
    @denominador.setter
    def denominador(self, valor):
        self._denominador = valor

    def esValid(self):
        return self._denominador != 0
    
    def simplifica(self):
        mcd = self._maximComuDivisor()
        self._numerador /= mcd
        self._denominador /= mcd
    
    def __add__(self, operand):
        resultat = NombreRacional()
        resultat.numerador = (self.numerador * operand.denominador) + (self.denominador * operand.numerador)
        resultat.denominador = self.denominador * operand.denominador
        resultat.simplifica()
        return resultat

    def __sub__(self, operand):
        resultat = NombreRacional()
        resultat.numerador = (self.numerador * operand.denominador) - (self.denominador * operand.numerador)
        resultat.denominador = self.denominador * operand.denominador
        resultat.simplifica()
        return resultat
    
    def __mul__(self, operand):
        resultat = NombreRacional()
        resultat.numerador = self.numerador * operand.numerador
        resultat.denominador = self.denominador * operand.denominador
        resultat.simplifica()
        return resultat

    def __truediv__(self, operand):
        resultat = NombreRacional()
        resultat.numerador = self.numerador * operand.denominador
        resultat.denominador = self.denominador * operand.numerador
        resultat.simplifica()
        return resultat

    def _maximComuDivisor(self):
        n1 = self._numerador
        n2 = self._denominador
        if n2 > n1:
            tmp = n2
            n2 = n1
            n1 = tmp
        while n2 != 0:
            tmp = n2
            n2 = n1 % n2
            n1 = tmp;
        return n1;


def operar(llistaRacionals, operacio, operand):
    resultat = []
    for r in llistaRacionals:
        if r.esValid():
            if operacio == '+':
                resultat.append(r + operand)
            elif operacio == '-':
                resultat.append(r - operand)
            elif operacio == '*':
                resultat.append(r * operand)
            else:
                resultat.append(r / operand)    
        else:
            resultat.append(NombreRacional())
    return resultat