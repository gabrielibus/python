# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:38:55 2019

@author: CompuFacilito
"""

def filtrarPalabras_(x,n):
    inicio = x[0]
    for i in x:
        if len(i) > n:
            print(i)
    

x = ("holsa","feo","ochos","mocho","nich")
n = 4
filtrarPalabras_(x,n)