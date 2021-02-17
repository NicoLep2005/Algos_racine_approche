# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:16:19 2021

@author: PC Fixe Nicolas
"""

from math import *

#definition d'une fonction g(x)

def g(x):
    return log(x) + x**2

#algo dichotomique pour fonction continue, basée sur le corollaire du TVI

def methode_dichotomie(a,b):
    half = (a+b)/2
    if (b-a) <= 10**-2:
        return round(half, 2)
    else:
        if g(half)*g(b)>0:
            return methode_dichotomie(a, half)
        else:
            return methode_dichotomie(half, b)