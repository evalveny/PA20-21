


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:31:25 2019

@author: Ernest
"""
import punt
import poligon
     
grade = 0
print ("Grade :=>>", grade)

print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>> ")

print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Iniciant test de la classe Poligon")
print ("Comment :=>> ----------------------------------")
reduccio = 0
vertexs = [punt.Punt(0,0), punt.Punt(0,1), punt.Punt(1,1), punt.Punt(1,0)]
vertexs_list = [(0,0), (0,1), (1,1), (1,0)]
perimetre_esperat = 4
print ("Comment :=>> ")
print ("Comment :=>> Creant poligon amb vertexs: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
pol = poligon.Poligon(vertexs)
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
perimetre = pol.perimetre()
print ("Comment :=>> Resultat esperat: ", perimetre_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", perimetre)
if (perimetre == perimetre_esperat):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    area = pol.area()
    error = True
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = False
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0

grade = grade + (2 - reduccio)
print ("Comment :=>> ")
print ("Grade :=>>", grade)
        
print ("Comment :=>> ")
print ("Comment :=>> -----------------------------------")
print ("Comment :=>> Iniciant test de la classe Triangle")
print ("Comment :=>> -----------------------------------")
reduccio = 0
vertexs = [punt.Punt(0,0), punt.Punt(0,1), punt.Punt(1,1), punt.Punt(1,0)]
vertexs_list = [(0,0, (0,1), (1,1), (1,0))]
print ("Comment :=>> ")
print ("Comment :=>> Creant triangle amb vertexs: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    trgle = poligon.Triangle(vertexs)
    print ("Comment :=>> Resultat obtingut: TRIANGLE CREAT")
    error = True
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = False
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

vertexs = [punt.Punt(0,0), punt.Punt(0,1), punt.Punt(1,1)]
vertexs_list = [(0,0), (0,1), (1,1)]
perimetre_esperat = 3.4142
area_esperada = 0.5
print ("Comment :=>> ")
print ("Comment :=>> Creant triangle amb vertexs: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: TRIANGLE CREAT")
print ("Comment :=>> ---")
try:
    trgle = poligon.Triangle(vertexs)
    print ("Comment :=>> Resultat obtingut: TRIANGLE CREAT")
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
        
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode afegeix_vertex: ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    trgle.afegeix_vertex(punt.Punt(0,0))
    print ("Comment :=>> Resultat obtingut: VERTEX AFEGIT")
    error = True
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = False
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
perimetre = trgle.perimetre()
print ("Comment :=>> Resultat esperat: ", perimetre_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", perimetre)
if (abs(perimetre - perimetre_esperat) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat:", area_esperada)
print ("Comment :=>> ---")
try:
    area = trgle.area()
    error = False
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = True
    area = 0.5
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error and (abs(area - area_esperada) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

grade = grade + (3 - reduccio)
print ("Grade :=>>", grade)

print ("Comment :=>> ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Iniciant test de la classe Quadrat")
print ("Comment :=>> ----------------------------------")
reduccio = 0
vertexs = [punt.Punt(0,0), punt.Punt(0,1), punt.Punt(1,1), punt.Punt(1,3)]
vertexs_list = [(0,0), (0,1), (1,1), (1,3)]
print ("Comment :=>> ")
print ("Comment :=>> Creant quadrat amb vertexs: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    qdrat = poligon.Quadrat(vertexs)
    print ("Comment :=>> Resultat obtingut: QUADRAT CREAT")
    error = True
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = False
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

vertexs = [punt.Punt(0,0), punt.Punt(0,1), punt.Punt(1,1), punt.Punt(1,0)]
vertexs_list = [(0,0), (0,1), (1,1), (1,0)]
perimetre_esperat = 4
area_esperada = 1
costat_esperat = 1
print ("Comment :=>> ")
print ("Comment :=>> Creant quadrat amb vertexs: ", vertexs_list)
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: QUADRAT CREAT")
print ("Comment :=>> ---")
try:
    qdrat = poligon.Quadrat(vertexs)
    print ("Comment :=>> Resultat obtingut: QUADRAT CREAT")
    error = False
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
        
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode afegeix_vertex: ")
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> Resultat esperat: EXCEPCIO")
print ("Comment :=>> ---")
try:
    qdrat.afegeix_vertex(punt.Punt(0,0))
    print ("Comment :=>> Resultat obtingut: VERTEX AFEGIT")
    error = True
except:
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
    error = False
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

print ("Comment :=>> ")
print ("Comment :=>> Recuperant el valor de la propietat 'costat'...")
print ("Comment :=>> -----------------------------------------------")
costat = qdrat.costat
print ("Comment :=>> Resultat esperat: ", costat_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", costat)
if (abs(costat - costat_esperat) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")


print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode perimetre...")
print ("Comment :=>> ------------------------------")
perimetre = qdrat.perimetre()
print ("Comment :=>> Resultat esperat: ", perimetre_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", perimetre)
if (abs(perimetre - perimetre_esperat) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
print ("Comment :=>> ")
print ("Comment :=>> Cridant al metode area...")
print ("Comment :=>> ------------------------")
print ("Comment :=>> Resultat esperat:", area_esperada)
print ("Comment :=>> ---")
try:
    area = qdrat.area()
    error = False
    print ("Comment :=>> Resultat obtingut: ", area)
except:
    error = True
    area = 0.5
    print ("Comment :=>> Resultat obtingut: EXCEPCIO")
if not error and (abs(area - area_esperada) < 0.01):
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")

grade = grade + (3 - reduccio)
print ("Grade :=>>", grade)

print ("Comment :=>> ")
print ("Comment :=>> ---------------------------------------")
print ("Comment :=>> Iniciant test de la funció test_poligon")
print ("Comment :=>> ---------------------------------------")
print ("Comment :=>> ")
print ("Comment :=>> Cridant a la funció llegeix_poligons amb el fitxer dades_poligons.txt")
print ("Comment :=>> ----------------------------------------------------------------------")
poligons = poligon.llegeix_poligons('dades_poligons.txt')
print ("Comment :=>> Cridant a la funció test_poligons amb el resultat de la crida anterior")
print ("Comment :=>> ----------------------------------------------------------------------")
print ("Comment :=>> ")
resultat = poligon.test_poligon(poligons)
resultat_esperat = [(4.0, -1), (3.414213562373095, 0.5), (4.0, 1.0)]
print ("Comment :=>> Resultat esperat:", resultat_esperat)
print ("Comment :=>> ---")
print ("Comment :=>> Resultat obtingut: ", resultat)
error = False
for r, re in zip(resultat, resultat_esperat):
    if (abs(r[0] - re[0]) > 0.01) or (abs(r[1] - re[1]) > 0.01):
        error = True
if not error:
    print ("Comment :=>> CORRECTE")
else:
    print ("Comment :=>> ERROR")
    reduccio = reduccio + 2.0
print ("Comment :=>> ----------------------------------")
grade = grade + (2 - reduccio)

if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)
print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")




