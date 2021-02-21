# -*- coding: utf-8 -*-
import exercici

grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")

reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio suma_acumulada" )
llista = [[1, 2, 3, 4], [], [1], [4, 3, 2, 1]]
sumaEsperada = [[1, 3, 6, 10], [], [1], [4, 7, 9, 10]]
for i, l in enumerate(llista):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Llista Original: ", l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", sumaEsperada[i])
    resultat = exercici.suma_acumulada(l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == sumaEsperada[i]):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0       
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)

reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio factorial_llista" )
llista = [[1, 2, 3, 4], [], [4], [5, 3, 6]]
factorialEsperat = [[1, 2, 6, 24], [], [24], [120, 6, 720]]
for i, l in enumerate(llista):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Llista Original: ", l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", factorialEsperat[i])
    resultat = exercici.factorial_llista(l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == factorialEsperat[i]):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio primers" )
llista = [[1, 2, 3, 4], [], [4], [5, 23, 15, 3, 37, 49]]
primersEsperats = [[1, 2, 3], [], [], [5, 23, 3, 37]]
for i, l in enumerate(llista):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Llista Original: ", l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", primersEsperats[i])
    resultat = exercici.primers(l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == primersEsperats[i]):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0      
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio elimina_duplicats" )
llista = [[1, 2, 3, 4], [], [4, 4, 4, 4], [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]]
noDuplicatsEsperat = [[1, 2, 3, 4], [], [4], [5, 4, 3, 2, 1]]
for i, l in enumerate(llista):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Llista Original: ", l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", noDuplicatsEsperat[i])
    resultat = exercici.elimina_duplicats(l)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == noDuplicatsEsperat[i]):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0      
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio binari_decimal" )
binari = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], 
          [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],
		  [0, 0, 1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 1, 1]]
decimalEsperat = [-1, 0, -6, 6, -86, 85, 42, -117]
for i, b in enumerate(binari):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i+1)
    print("Comment :=>> Numero binari: ", b)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", decimalEsperat[i])
    resultat = exercici.binari_decimal(b)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == decimalEsperat[i]):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0      
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2.0 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
