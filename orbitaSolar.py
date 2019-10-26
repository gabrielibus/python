# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:05:40 2019

@author: CompuFacilito
"""

# coding: utf-8

# In[2]:


import numpy as np 
from matplotlib import pyplot as plt    #Libreria para gráficos y estadística
from math import pi                     #Valor de pi 

plt.rcParams["figure.figsize"] = [9,9]  #Tamaño de la gráfica


# Definir semieje mayor (distancia media, o semieje mayor) y excentricidad de la orbita
a = np.array([0.39,0.72,1.0,1.52,5.2,9.54,19.18,30.06,39.2])
e = np.array([0.2056, 0.0068,0.0167,0.0934,0.0483,0.0560, 0.0461, 0.0097,0.244])


# Calcular el semieje menor a partir de a y e
b=[]
for i in range(len(a)):
    
    bi = a[i]*np.sqrt(1-e[i]**2)
    b.append(bi)

# Coordenadas (u,v) del centro de la elipse
u=0.  
v=0. 

#Graficas de las elipses
N=len(a)
ni=0
N=9
for i in range(ni,N):
    
    # Parametro theta para resolver la ecuación de la elipse (angulo)
    theta = np.linspace(0, 2*pi, 100) 
    
    #Distancia del centro de la elipse al foco positivo
    c = np.sqrt(a[i]**2 - b[i]**2)
    
    plt.plot(c,0,'*', markersize=15)               #Posicion del foco
    
    plt.plot(u+a[i]*np.cos(theta) , v+b[i]*np.sin(theta))  
    plt.xlim(-max(a[i]*np.cos(theta)), max(a[i]*np.cos(theta)))
    plt.ylim(-max(a[i]*np.cos(theta)), max(a[i]*np.cos(theta)))
    plt.grid(color='lightgray',linestyle='--') 
    