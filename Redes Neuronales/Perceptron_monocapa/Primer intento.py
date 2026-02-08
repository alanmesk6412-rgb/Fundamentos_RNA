import numpy as np
import matplotlib as plt
"""
ESTA CLASE NEURONA TIENE COMO PARÁMETROS:
- MATRIZ DE DATOS
- PESOS Y BIAS
- TASA DE APRENDIZAJE
TIENE COMO MÉTODOS:
- NET_J (producto entre una fila de la matriz de datos y el vector de pesos con bias)
- F (Función que se aplica a NET_J para introducir la no linealidad)
- AJUSTES (de pesos y bias)
"""

class neurona:
  def __init__(self, pesos = None, datos = None,salidas = None, tasa = 0.05):
    self.pesos = open(r"C:\Users\PC\Desktop\Redes Neuronales\Perceptron_monocapa\2_pesos.txt","r+")
    self.datos = open(r"C:\Users\PC\Desktop\Redes Neuronales\Perceptron_monocapa\1_entradas.txt")
    self.salidas = open(r"C:\Users\PC\Desktop\Redes Neuronales\Perceptron_monocapa\3_salidas.txt")
    self.tasa = 0.05
  
  def interacion(self):
    lectura_d = "r"
    while lectura_d != '':
      #PREPARAR DATOS DE ENTRENAMIENTO
      salida = self.salidas.readline().astype(int)
      # PREPARAR LA FILA DE LA MATRIZ DE DATOS
      lectura_d = self.datos.readline()
      fila = np.array(lectura_d.split(","))
      ## PREPARAR EL VECTOR DE PESOS
      vector = self.pesos.readline()
      vector = np.array(vector.split(","))
      ### COMENZAR A ACTIVAR Y AJUSTAR
      y = np.heaviside(fila @ vector,0)
      vector[0] = vector[0] + self.tasa *(salida - y)
      vector[1] = vector[1] + self.tasa *(salida - y)
      vector[2] = vector[2] + self.tasa * (salida - y)
      w1 = str(vector[0])
      w2 = str(vector[1])
      b = str(vector[2])
      self.pesos.writeline("w1,w2,b")
    return self.pesos


N = neurona()

print(type(N.pesos.readline()))
print(N.pesos.readline())



    









