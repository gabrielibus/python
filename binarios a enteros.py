# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:27:42 2019

@author: CompuFacilito
"""

binario = input("ingrese el número binario correspondiente: --> ")
valor = 0
resultado = 0
potencia = len(binario) - 1
for i in binario:
    valor = int(i) * (2 ** potencia)
    potencia -= 1
    resultado = resultado + valor
print(resultado)