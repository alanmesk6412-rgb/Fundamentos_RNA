import pandas as pd
import numpy as np

#Primero extraemos los datos del .csv que creamos con la tabla de OR
Data = pd.read_csv(r"C:\Users\PC\Desktop\RedesNeuronales\Adaline\Data.csv", sep=r"\s+")
#Ahora preparamos nuestros datos:
"""
  (0) Factor de aprendizaje y error
  (1) Vector inicial de pesos y bias W
  (2) Matriz de datos extendida X
  (3) Vector de datos esperados T
"""
a = 0.1
err = 10
errpass = 0

W = np.array([0.1,0.1,0.1])

X = Data[['x1','x2']].to_numpy()
x = np.array([1,1,1,1])
X = np.column_stack((X,x))

T = Data['t'].to_numpy()


Y = np.array([0,0,0,0])


while err>=0.00001:
  Y= X@W
  E = T - Y
  W = W + a*((np.transpose(X))@E)
  err = np.abs(np.linalg.norm(E,ord=np.inf) - errpass)
  errpass = np.linalg.norm(E, ord=np.inf)

print(np.sign(Y))
print(X)

