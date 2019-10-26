def invertirCadena(x):
    contador = 1
    res = ""
    for i in x:
        y = len(x) - contador
        contador += 1
        res = res + x[y]
    return res
#    print(resultado)
#    return resultado

x = "radar"
if x == invertirCadena(x):
    print("Soy palíndromo")
else:
    print("Inténtalo nuevamente")
