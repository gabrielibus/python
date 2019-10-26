# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:23:57 2019

@author: CompuFacilito
"""

def contarVocales():
    x = input("Ingrese el texto que desea analizar --> ")
    y =("a","e","i","o","u")
    a,e,i,o,u = 0,0,0,0,0    
    for i in x:
        if i == "a":
            a += 1
        elif i == "e":
            e += 1
        elif i == "i":
            i += 1
        elif i == "o":
            o += 1
        elif i == "u":
            u += 1
    print("'a' está: "+str(a)+" veces.")
    print("'e' está: "+str(a)+" veces.")
    print("'i' está: "+str(a)+" veces.")
    print("'o' está: "+str(a)+" veces.")
    print("'u' está: "+str(a)+" veces.")

contarVocales()