# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:34:17 2019

@author: CompuFacilito
"""

def esBisiesto(x):
    año = x
    if type(año / 4) == int:
        if type(año / 100) == int and type(año / 400) == int:
            print("verdadero")
    else:
        print("falso")
    print(año)    
    print(año / 400)
esBisiesto(2000)