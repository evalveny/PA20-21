# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:25:14 2021

@author: 1002245
"""

class NumeroComplex:
    def __init__(self, p_real = 0, p_img = 0):
        self._real = p_real
        self._img = p_img
    
    def get_real(self):
        return self._real
    
    def get_img(self):
        return self._img
    
    def set_real(self, real):
        self._real = real
    
    def set_img(self, img):
        self._img = img
        
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

def principal():
    opcio = 0
    c1 = NumeroComplex()
    c2 = NumeroComplex()
    while (opcio != '5'):
        opcio = input ("Introdueix una opcio (1. Suma, 2. Resta, 3. Multiplicacio, 4. Conjugat, 5. Sortir): ")
        if (opcio == '1'):
            c1.set_real(float(input('Part real: ')))
            c1.set_img(float(input('Part imaginaria: ')))
            c2.set_real(float(input('Part real: ')))
            c2.set_img(float(input('Part imaginaria: ')))
            resultat = c1 + c2
            print ("Resultat de la suma: ", str(resultat.get_real()) + '+' + str(resultat.get_img()) + 'i')
        elif (opcio == '2'):
            c1.set_real(float(input('Part real: ')))
            c1.set_img(float(input('Part imaginaria: ')))
            c2.set_real(float(input('Part real: ')))
            c2.set_img(float(input('Part imaginaria: ')))
            resultat = c1 - c2
            print ("Resultat de la resta: ", str(resultat.get_real()) + '+' + str(resultat.get_img()) + 'i')
        elif (opcio == '3'):
            c1.set_real(float(input('Part real: ')))
            c1.set_img(float(input('Part imaginaria: ')))
            c2.set_real(float(input('Part real: ')))
            c2.set_img(float(input('Part imaginaria: ')))
            resultat = c1 * c2
            print ("Resultat de la multiplicacio: ", str(resultat.get_real()) + '+' + str(resultat.get_img()) + 'i')
        elif (opcio == '4'):
            c1.set_real(float(input('Part real: ')))
            c1.set_img(float(input('Part imaginaria: ')))
            resultat = c1.conjugat()
            print ("Conjugat", str(resultat.get_real()) + '+' + str(resultat.get_img()) + 'i')
        elif (opcio != '5'):
            print ("Opcio incorrecta")
          
if __name__ == "__main__":
    principal()