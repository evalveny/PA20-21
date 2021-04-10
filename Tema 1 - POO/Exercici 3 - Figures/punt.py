# -*- coding: utf-8 -*-

import math

class Point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, valor):
        self._x = valor

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, valor):
        self._y = valor
    
    def __sub__(self,p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
       
    def __str__(self):  
        return "("+ str(self.x) + ", " + str(self.y) + ")"