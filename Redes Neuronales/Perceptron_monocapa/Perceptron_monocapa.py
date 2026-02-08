import numpy as np
import os
def eval(N,W):
  print(np.dot(N,W))
  y = np.heaviside(np.dot(N,W),0)
  return y
"""
ESTA ES UNA RED NEURONAL QUE APRENDE LA TABLA DE VERDAD DE LA CONJUNCIÓN
"""

entradas = open(r"C:\Users\PC\Desktop\Redes Neuronales\Perceptron_monocapa\1_entradas.txt")
pesos = open(r"C:\Users\PC\Desktop\Redes Neuronales\Perceptron_monocapa\2_pesos.txt","r+")
salidas = open(r"Perceptron_monocapa/3_salidas.txt")


P = pesos.readline()
W = np.array([float(num) for num in P.split(",")])
W_o = np.array([float(num) for num in P.split(",")])

Q = salidas.readline()
Y = np.array([float(num) for num in Q.split(",")])

t = 0.05

print(W)
N = np.array([1.,1.,1.])
print(f"EL RESULTADO ANTES DEL APRENDIZAJE ES: {eval(N,W)}")
print(Y[3])

print("======================================================================================")
for j in range(3):
  k=0
  print("PRIMERA ITERACIÓN")
  entradas.seek(0)
  for linea in entradas:
    print(f"Linea {k}")
    X = np.array([float(num) for num in linea.split(",")])

    y = np.heaviside(np.dot(X,W),0)
    print("COMIENZO DE AJUSTES")
    for i in range(3):
      W[i] = W[i] + t*(Y[k] -y)
      print(Y[k])
    k = k+1
    
    print("FIN DE AJUSTES")



print("======================================================================================")
print(W)
print(F"EL RESULTADO DESPUÉS DEL APRENDIZAJE ES: {eval(N,W)}")



