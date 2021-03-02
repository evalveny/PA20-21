# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:45:32 2021

@author: 1002245
"""

class NumeroComplex:
    def __init__(self, p_real = 0, p_img = 0):
        self._real = p_real
        self._img = p_img
    
    def conjugat(self):
        return NumeroComplex(self._real, -self._img)
    
    def __add__(self, c):
        return NumeroComplex(self._real + c._real, self._img + c._img)
    
    def __sub__(self, c):
        return NumeroComplex(self._real - c._real, self._img - c._img)
    
    def __mul__(self, c):
        real = self._real*c._real - self._img*c._img
        img = self._real*c._img + self._img*c._real
        return NumeroComplex(real, img)

c = NumeroComplex()

c._real = float(input())
c._img = float(input())

conj = c.conjugat()

print(conj._real, conj._img)