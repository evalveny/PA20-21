# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:02:10 2021

@author: 1002245
"""

class NumeroComplex:
    def __init__(self, p_real = 0, p_img = 0):
        self.valors = [p_real, p_img]
        
    def conjugat(self):
        return NumeroComplex(self.valors[0], -self.valors[1])
    
    def __add__(self, c):
        return NumeroComplex(self.valors[0] + c.valors[0], self.valors[1] + c.valors[1])
    
    def __sub__(self, c):
        return NumeroComplex(self.valors[0] - c.valors[0], self.valors[1] - c.valors[1])
    
    def __mul__(self, c):
        real = self.valors[0]*c.valors[0] - self.valors[1]*c.valors[1]
        img = self.valors[0]*c.valors[1] + self.valors[1]*c.valors[0]
        return NumeroComplex(real, img)

def principal():
    opcio = 0
    c1 = NumeroComplex()
    c2 = NumeroComplex()
    while (opcio != '5'):
        opcio = input ("Introdueix una opcio (1. Suma, 2. Resta, 3. Multiplicacio, 4. Conjugat, 5. Sortir): ")
        if (opcio == '1'):
            c1.real = float(input('Part real: '))
            c1.img = float(input('Part imaginaria: '))
            c2.real = float(input('Part real: '))
            c2.img = float(input('Part imaginaria: '))
            resultat = c1 + c2
            print ("Resultat de la suma: ", str(resultat.real) + '+' + str(resultat.img) + 'i')
        elif (opcio == '2'):
            c1.real = float(input('Part real: '))
            c1.img = float(input('Part imaginaria: '))
            c2.real = float(input('Part real: '))
            c2.img = float(input('Part imaginaria: '))
            resultat = c1 - c2
            print ("Resultat de la resta: ", str(resultat.real) + '+' + str(resultat.img) + 'i')
        elif (opcio == '3'):
            c1.real = float(input('Part real: '))
            c1.img = float(input('Part imaginaria: '))
            c2.real = float(input('Part real: '))
            c2.img = float(input('Part imaginaria: '))
            resultat = c1 * c2
            print ("Resultat de la multiplicacio: ", str(resultat.real) + '+' + str(resultat.img) + 'i')
        elif (opcio == '4'):
            c1.real = float(input('Part real: '))
            c1.img = float(input('Part imaginaria: '))
            resultat = c1.conjugat()
            print ("Conjugat", str(resultat.real) + '+' + str(resultat.img) + 'i')
        elif (opcio != '5'):
            print ("Opcio incorrecta")
          
if __name__ == "__main__":
    principal()