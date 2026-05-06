import numpy as np
import pandas as pd
#Primero agreguemos nuestros datos
Data = pd.read_csv(r"C:\Users\PC\Desktop\RedesNeuronales\Madaline\DataMadaline.csv", sep=r"\s+")
#Preparemos nuestros datos
"""
  (1) Crear matriz de datos extendida X
  (2) Crear el vector de salidas esperadas Y
  (3) Crear matriz de pesos extendida W y V  (bias = 1)
  (4) Establecer la taza de aprendizaje y als variables de error
"""
X = Data[["x1","x2"]].to_numpy()
X = np.column_stack((X,np.array([1,1,1])))

Y = Data["t"].to_numpy()

W = np.array([[0.1,0.1,1],[0.1,0.1,1]])
V = np.array([0.5,0.5,1])

a = 0.1
err = 10
errpass = 0

"""
  (5) Ahora comenzaremos la implementación de el algoritmo de épocas
      utilicemos la matriz vacía T para guardar los valores
"""
T = np.array([[0,0],[0,0]])

while err>=0.0000001:
  Z = X@(np.transpose(W))
  Z = np.column_stack((Z,np.array([1,1,1])))
  T = Z@V
  E = Y - T
  W = W + a*(np.transpose(X))@(E)
  err = np.abs((np.linalg.norm(E, ord = np.inf) - errpass))
  errpass = np.linalg.norm(E, ord = np.inf)

print(np.sign(T))
print(Y)