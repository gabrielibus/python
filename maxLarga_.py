# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:23:21 2019

@author: CompuFacilito
"""

def maxLarga(x):
    inicio = x[0]
    for i in x:
        if len(i) > len(inicio):
            inicio = i
    print(inicio)
    
    
    
x = ("gabrielito","mafe","carlos","danielito")

maxLarga(x)