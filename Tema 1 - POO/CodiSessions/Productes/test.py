# -*- coding: utf-8 -*-

import producte
      
grade = 0
reduccio = 0.0
print ("Grade :=>>", grade)


print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")

l_llibres_esperat = [('CODI_1', 10, 'TITOL_1', 'AUTOR_1', 100, 1.0),
                     ('CODI_3', 30, 'TITOL_3', 'AUTOR_3', 300, 1.0),
                     ('CODI_4', 40, 'TITOL_4', 'AUTOR_4', 400, 1.0),
                     ('CODI_6', 60, 'TITOL_6', 'AUTOR_6', 600, 2.0)]

l_elec_esperat = [('CODI_2', 200, 'MARCA_2', 'MODEL_2', 20, 3.0),
                   ('CODI_5', 500, 'MARCA_5', 'MODEL_5', 50, 7.0)]

print ("Comment :=>> ========================================================")
print ("Comment :=>> Llegint fitxer de productes productes.txt ")
print ("Comment :=>> Crida a la funcio llegeix_productes ")
print ("Comment :=>> ")
l_llibres, l_elec = producte.llegeix_productes('productes.txt')

print ("Comment :=>> ---------------------------------")
print ("Comment :=>> Comprovant dades dels llibres")
l_llibres[0].afegeix_valoracio(5, "text valoracio")
for i, le in enumerate(l_llibres_esperat):
    print ("Comment :=>> Resultat esperat llibre: ", i)
    print ("Comment :=>> Codi, Preu, Titol, Autor, N. Pagines, Despeses: ")
    print ("Comment :=>> ", le)    
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ")
    l = l_llibres[i]
    l_valors = (l.codi, l.preu, l.titol, l.autor, l.n_pagines, l.despeses_enviament())
    print ("Comment :=>> Codi, Preu, Titol, Autor, N. Pagines, Despeses: ")
    print ("Comment :=>> ", l_valors)
    print ("Comment :=>> ---")
    if (le == l_valors):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio += 2.0
    print ("Comment :=>> ---------------")
    if len(l_llibres_esperat) != len(l_llibres):
        print ("Comment :=>> ERROR. Nº de llibres obtingut diferent a l'esperat")
        reduccio += 2.0
grade = grade + 5.0 - reduccio
if grade < 0:
    grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> ---------------------------------")
print ("Comment :=>> Comprovant dades dels electrodomestics")
l_elec[0].afegeix_distribuidor("nom distribuidor")
for i, ee in enumerate(l_elec_esperat):
    print ("Comment :=>> Resultat esperat electrodomestic: ", i)
    print ("Comment :=>> Codi, Preu, Marca, Model, Volum, Despeses: ")
    print ("Comment :=>> ", ee)    
    print ("Comment :=>> ---")
    print ("Comment :=>> Resultat obtingut: ")
    e = l_elec[i]
    e_valors = (e.codi, e.preu, e.marca, e.model, e.volum, e.despeses_enviament())
    print ("Comment :=>> Codi, Preu, Marca, M0odel, Volum, Despeses: ")
    print ("Comment :=>> ", e_valors)
    print ("Comment :=>> ---")
    if (ee == e_valors):    
        print ("Comment :=>> CORRECTE")
    else:
        print ("Comment :=>> ERROR")
        reduccio += 2.0
    print ("Comment :=>> ---------------")
    if len(l_elec_esperat) != len(l_elec):
        print ("Comment :=>> ERROR. Nº d'electrodomestics obtingut diferent a l'esperat")
        reduccio += 2.0
grade = grade + 5.0 - reduccio
if grade < 0:
    grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
