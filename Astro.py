import math

print("Calculo del radio de la tierra")

h = float(input("Altura del gnomon en cm --> "))
s = float(input("Longitud de la sombra en cm --> "))
l = float(input("Distancia entre UdeA y locación 'sin sombra' en km --> "))

a = (math.atan(s / h))
r = (l / a)

print("El radio de la tierra medido es: ", r, " km")
