# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:13:14 2020

@author: Ernest
"""
class Data:
    def __init__(self, dia = 0, mes = 0, any = 0):
        self.dia = dia
        self.mes = mes
        self.any = any
        self.dies_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def es_traspas(self):
        return (self.any % 4) == 0 and ((self.any % 100) != 0 or (self.any % 400) == 0)
    
    def es_valida(self):
        dies_mes = self.dies_mes[self.mes - 1]
        if self.es_traspas() and self.mes == 2:
            dies_mes += 1
        return 1 <= self.mes and self.mes <= 12 and 1 <= self.any and 1 <= self.dia and self.dia <= dies_mes

    def __lt__(self, data):
        menor = False
        if self.any < data.any:
            menor = True
        elif self.any == data.any:
            if self.mes < data.mes:
                menor = True
            elif self.mes == data.mes:
                menor = (self.dia < data.dia)
        return menor
    
    def __eq__(self, data):
        return self.any == data.any and self.mes == data.mes and self.dia == data.dia
    
    def __add__(self, n_dies):
        data_resultat = Data(self.dia, self.mes, self.any)
        while (n_dies > 0):
            dies_mes = data_resultat.dies_mes[data_resultat.mes - 1]
            if data_resultat.es_traspas():
                dies_mes += 1
            if ((data_resultat.dia + n_dies) > dies_mes):
                n_dies -= (dies_mes - data_resultat.dia) + 1
                data_resultat.dia = 1
                data_resultat.mes += 1
                if (data_resultat.mes > 12):
                    data_resultat.mes = 1
                    data_resultat.any += 1
            else:
                data_resultat.dia += n_dies
                n_dies = 0
        return data_resultat
        
    def __str__(self):
        return '{dia:02d}/{mes:02d}/{any:04d}'.format(dia = self.dia, mes=self.mes, any=self.any)


def termini_valid(dia_original, n_dies, data_actual):
    if (not dia_original.es_valida()) or (not data_actual.es_valida()):
        raise ValueError
    dia_termini = dia_original + n_dies
    if data_actual < dia_termini or data_actual == dia_termini:
        valid = True
    else:
        valid = False
    return valid
