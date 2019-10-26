# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:17:59 2019

@author: CompuFacilito
"""
import random

n = input("Ingrese el número de cifras a adivinar: ")

cont = int(n)

cadena = []
x = int(n)
cadena.append(random.randrange(x))
#while cont > 0:
#    cadena.append(random.randrange(n*9))
#    cont -= 1
#    
#print(cadena)