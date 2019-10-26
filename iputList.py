# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:57:35 2019

@author: CompuFacilito
"""
Lista = []
L = input("Ingrese la lista correspondiente separadndo los elementos por coma: ")
a = 0
for i in L:
    if i == "," or i == " ":
        pass
    else:
        a = int(i)
        Lista.append(a)

print(Lista)