# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:11:12 2019

@author: CompuFacilito
"""

year = input("Ingrese el año en curso p.ej: 1999 --> ")
nombre1 = input ("Ingrese el nombre del primer usuario y el año de nacimiento separados por punto y coma ; p. ej. Gabriel López;1982 --> ")
#nombre2 = input ("Ingrese el nombre del segundo usuario y el año de nacimiento separados por punto y coma ; p. ej. Gabriel López;1982 --> ")
#nombre3 = input ("Ingrese el nombre del tercer usuario y el año de nacimiento separados por punto y coma ;23 p. ej. Gabriel López;1982 --> ")

edad1 = - int(nombre1) + int(year)

print(edad1)
