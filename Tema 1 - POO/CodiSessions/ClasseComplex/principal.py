# -*- coding: utf-8 -*-

import complex

def principal():
    opcio = 0
    c1 = complex.NumeroComplex()
    c2 = complex.NumeroComplex()
    while (opcio != '5'):
        opcio = input ("Introdueix una opcio (1. Suma, 2. Resta, 3. Multiplicacio, 4. Conjugat, 5. Sortir): ")
        if (opcio == '1'):
            c1.llegeix()
            c2.llegeix()
            print ("Resultat de la suma: ", c1 + c2)
        elif (opcio == '2'):
            c1.llegeix()
            c2.llegeix()
            print ("Resultat de la resta: ", c1 - c2)
        elif (opcio == '3'):
            c1.llegeix()
            c2.llegeix()
            print ("Resultat de la multiplicacio: ", c1 * c2)
        elif (opcio == '4'):
            c1.llegeix()
            print ("Conjugat", c1.conjugat())
        elif (opcio != '5'):
            print ("Opcio incorrecta")

          
if __name__ == "__main__":
    principal()

