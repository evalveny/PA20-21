# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:10:57 2019

@author: ernest
"""
import complex 

c = complex.NumeroComplex()

c.real = float(input())
c.img = float(input())

conj = c.conjugat()

print (conj.real, conj.img)
