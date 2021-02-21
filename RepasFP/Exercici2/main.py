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
print ("Comment :=>> Test de la funcio interseccio" )
llista1 = [[1, 2, 3, 4], [1, 2], [], [1, 2], [4, 3, 2, 1]]
llista2 = [[2, 3, 5], [1, 2], [1, 2], [], [5, 6]]
llistaEsperada = [[2, 3], [1, 2], [], [], []]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.interseccio(l1, l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0   
    i = i+1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)

reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio unio" )
llista1 = [[1, 2, 3, 4], [1, 2], [], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1, 2], [1, 2], [], [5, 6]]
llistaEsperada = [[1, 2, 3, 4, 0, 5], [1, 2], [1, 2], [1, 2], [4, 3, 2, 1, 5, 6]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.unio(l1, l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0 
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio multiplicacio_llistes" )
llista1 = [[1, 2, 3, 4], [1, 2], [2], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1], [1, 2], [], [5, 6]]
llistaEsperada = [[0, 4, 9, 20], [1], [2], [], [20, 18]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", le)
    resultat = exercici.multiplicacio_llistes(l1, l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut ", resultat)
    if (resultat == le):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0 
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio multiplicacio_elements" )
llista1 = [[1, 2, 3, 4], [1, 2], [2], [1, 2], [4, 3, 2, 1]]
llista2 = [[0, 2, 3, 5], [1], [1, 2], [], [5, 6]]
llistaEsperada = [[[0, 2, 3, 5], [0, 4, 6, 10], [0, 6, 9, 15], [0, 8, 12, 20]], [[1], [2]], [[2, 4]], [[], []], [[20, 24], [15, 18], [10, 12], [5,6]]]
i = 1
for l1, l2, le in zip(llista1, llista2, llistaEsperada):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ")
    for x in le:
        print (x)
    resultat = exercici.multiplicacio_elements(l1, l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ")
    for x in resultat:
        print(x)
    if (resultat == le):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0 
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)


reduccio = 0
print ("Comment :=>> ")
print ("Comment :=>> ========================================================")
print ("Comment :=>> Test de la funcio distancia_hamming" )
llista1 = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
llista2 = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
distancia_esperada = [0, 0, 4, 2, 1]
i = 1
for l1, l2, de in zip(llista1, llista2, distancia_esperada):
    print ("Comment :=>> ------------------------------------------")
    print("Comment :=>> Test: ", i)
    print("Comment :=>> Llista 1: ", l1)
    print("Comment :=>> Llista 2: ", l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat esperat: ", de)
    resultat = exercici.distancia_hamming(l1, l2)
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ", resultat)
    if (resultat == de):
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio = reduccio + 1.0 
    i = i + 1
if (reduccio > 4.0):
    reduccio = 4.0
grade = grade + (2 - reduccio)
if (grade < 0):
    grade = 0
print ("Grade :=>> ", grade)



print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
