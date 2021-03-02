# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:10:57 2019

@author: ernest
"""
class NumeroComplex:
    def __init__(self, p_real = 0, p_img = 0):
        self.real = p_real
        self.img = p_img
        
    def conjugat(self):
        return NumeroComplex(self.real, -self.img)
    
    def __add__(self, c):
        return NumeroComplex(self.real + c.real, self.img + c.img)
    
    def __sub__(self, c):
        return NumeroComplex(self.real - c.real, self.img - c.img)
    
    def __mul__(self, c):
        real = self.real*c.real - self.img*c.img
        img = self.real*c.img + self.img*c.real
        return NumeroComplex(real, img)

c = NumeroComplex()

c.real = float(input())
c.img = float(input())

conj = c.conjugat()

print(conj.real, conj.img)
