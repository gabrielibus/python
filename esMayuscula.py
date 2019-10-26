# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:39:24 2019

@author: CompuFacilito
"""

cadena = input("Ingrese el texto que desee analizar: ")
cont = 0
for i in cadena:
    if i.isupper() == True:
        cont += 1
print(cont)