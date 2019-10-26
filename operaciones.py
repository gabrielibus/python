#inicio
import numpy as np
ent1=1
ent2=2
real1=2.4
real2=2.4
comp1=2+3j
comp2=5-2j
cad1="pepe"
cad2="perez"
l1D1=[1,2,3]
l1D2=[4.5,2.2,3.0]
l2D1=[[1,2,3],[4,5,6],[7,8,9]]
l2D2=[[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]]
A1D1=np.array(l1D1)
A2D1=np.array(l1D2)
A2D2=np.array(l2D2)
print("Div entera",ent2//ent1)
print(":",3//2)
print("Div real",real2//real1)
print("concatenar:\n",cad1+cad2)
print("replicar:/n",3*cad1)
print("concatenar:/n",l1D1+l1D2)
print("replicar:/n",3*cad1)
print("uma de arreglos:",A1D1+A2D2)
print(A1D1)
print("producto por:",3*A1D1)
print("potencia por: ",A1D1**2)
print("potencia por: ",2**A1D1)
print("producto punto:",A1D1.dot(A2D2))


