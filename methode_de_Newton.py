# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:29:12 2021

@author: nicol
"""

from math import *

#définition d'une fonction g(x)

def g(x):
    return log(x) + x**2

#définition de sa dérivée

def dg(x):
    return 1/x + 2*x

#méthode de Newton basée sur les tangentes et beaucoup plus efficace que la dichotomie

def methode_de_Newton(x0):
    if abs(g(x0)/dg(x0)) >= 10**-2:      #on indique ici la précision voulue
        return methode_de_Newton(x0-(g(x0)/dg(x0)))
    else:
        return (round(x0, 2))            #on arrondit le résultat à x décimales près (on peut considérer ne pas être plus précis que la demandé au départ)

        
