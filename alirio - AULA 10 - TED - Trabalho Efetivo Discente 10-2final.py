#Faça um algoritmo para ler 50 números e armazenar em um vetor VET,/
#  verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.


from random import randint
from collections import Counter

lista = [randint(0, 9) for p in range(0, 50)]
print(lista)
c = Counter(lista)

for numero, repeticoes in c.items():
    if repeticoes > 1:
        result = [indice for indice, item in enumerate(lista) if item == numero]
        print(f'O número "{numero}" se repete nos índices {result}.')

