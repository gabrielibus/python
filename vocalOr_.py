# -*- coding: utf-8 -*-
#4- Escribir una función que tome un carácter 
#y devuelva True si es una vocal, 
#de lo contrario devuelve False.

def vocal(x):
#    x = list or str
    for x in x:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            print(x," es vocal")
        else:
            print(x," es consonante")
        
vocal("Murciélago")