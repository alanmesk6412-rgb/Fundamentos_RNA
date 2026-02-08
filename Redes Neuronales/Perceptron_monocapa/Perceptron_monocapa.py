import numpy as np

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
N = np.array([0.,0.,1.])
print("======================================================================================")
print(f"EL RESULTADO ANTES DEL APRENDIZAJE ES: {eval(N,W)}")
print("======================================================================================\n\n")
for j in range(3):
  k=0
  entradas.seek(0)
  for linea in entradas:
    X = np.array([float(num) for num in linea.split(",")])
    y = np.heaviside(np.dot(X,W),0)
    for i in range(3):
      W[i] = W[i] + t*(Y[k] -y)
    k = k+1

print("======================================================================================")
print(F"EL RESULTADO DESPUÉS DEL APRENDIZAJE ES: {eval(N,W)}")
print("======================================================================================")




