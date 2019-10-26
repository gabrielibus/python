# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:15:03 2019

@author: CompuFacilito
"""

user = input("ingrese las edades separadas por coma: ")
tupla = ()
for i in user:
    if i == "," or i == " ":
        pass
    else:
        a = int(i)
        tupla.append(a)

print(tupla)
print(user)
print(type(tupla))