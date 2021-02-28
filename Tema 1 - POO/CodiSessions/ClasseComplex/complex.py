# -*- coding: utf-8 -*-

class NumeroComplex:
    def __init__(self, p_real = 0, p_img = 0):
        self.real = p_real
        self.img = p_img
    
    def llegeix(self):
        self.real = float(input('Part real: '))
        self.img = float(input('Part imaginaria: '))
        
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
    
    def __str__(self):
        return str(self.real) + '+' + str(self.img) + 'i'
    
    