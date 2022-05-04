#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#Imprima o resultado da soma de todos os valores da matriz no terminal;
#E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint

a = []

for linha in range(10):
    linha = []
    for coluna in range(10):
        linha.append(randint(0, 10))
    a.append(linha)
    #print(a)

import numpy as np
 
def main():
  matriz = np.array([(a)])
   
  multiplicador = 3
  b = matriz * multiplicador
 
  print("Matriz inicial: ", matriz)
  print("Valor do multiplicador: ", multiplicador)
  print("Nova matriz: ", b)
 
if __name__== "__main__":
  main()

    

