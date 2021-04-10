# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:47:22 2020

@author: ernest
"""
import cercle
import triangle
import rectangle

def crea_figura(tipus):
    if (tipus == 'C'):
        fig = cercle.Cercle()
    elif (tipus == 'T'):
        fig = triangle.Triangle()
    elif (tipus == 'R'):
        fig = rectangle.Rectangle()
    else:
        raise Exception('Tipus de figura no valid')
    fig.llegeix()
    return fig


def suma_area(figures):
    area = [fig.area() for fig in figures]
    return sum(area)

def max_perimetre(figures):
    fig_max = max(figures, key = lambda f:f.perimetre())
    return fig_max

