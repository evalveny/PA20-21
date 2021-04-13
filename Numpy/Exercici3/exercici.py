# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:24:17 2018

@author: ernest
"""
import numpy as np
def mitjanaLliuraments(notes, estudiant):
    mitjana = 0
    notesEstudiant = notes[estudiant,:]
    totsFets = (notesEstudiant != -1).all()
    if (totsFets):
        mitjana = notesEstudiant.mean()
    return mitjana

def nAprovats(notes):
    notesMitjanes = [mitjanaLliuraments(notes, i) for i in range(notes.shape[0])]
    aprovats = [n for n in notesMitjanes if n >= 5]
    return len(aprovats)

def resultatExercici(notes, ex):
    notesEx = notes[:,ex]
    lliuraments = notesEx[notesEx != -1]
    return len(lliuraments), lliuraments.min(), lliuraments.max(), lliuraments.mean()

def abandonamentsSetmanals(notes):
    abandonaments = [0] * notes.shape[1]
    for estudiant in notes:
        for i in range(estudiant.size):
            if (estudiant[0:i] != -1).all() and (estudiant[i:] == -1).all():
                abandonaments[i] += 1
    return abandonaments
            