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

'''
méthode de Newton basée sur les tangentes et beaucoup plus efficace que la dichotomie 
(pour certaines raisons d'ensemble de définiton, si la valeur est trop éloignée, la methode peut ne pas fonctionner)
'''

def methode_de_Newton(x0):               #on fait passer en argument valeur proche de la racine (attention aux domaines de définition !)
    if abs(g(x0)/dg(x0)) >= 10**-3:      #on indique ici la précision voulue
        return methode_de_Newton(x0-(g(x0)/dg(x0)))
    else:
        return (round(x0, 2))            #on arrondit le résultat à x décimales près (on peut considérer ne pas être plus précis que demandé au départ)

        
