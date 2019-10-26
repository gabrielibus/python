# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:23:57 2019

@author: compuFacilito
"""

def contarVocales():
    texto = input("aIngrese el texto que desea analizar --> ")
    texto = texto.lower()
    vocales = ("aeiou")
    
    for i in vocales:
        cont = 0
        for n in texto:
            if n == i:
                cont += 1 
#            print("Hay %d %s." % (contador, x))
        print(i+" está presente "+str(cont)+" veces")
                
contarVocales()