'''Faça um vetor para ler 20 números e em um deles.
Após a leitura total dos 20 números, o que escrever deve escrever
esses 20 números lidos na ordem inversa.'''


import random
lista_de_numeros  = []
for  n  in  range (0 , 20):
    lista_de_numeros.append(random.randint(0, 50 ))
print ( f'Lista de Números: { lista_de_numeros } ' )
lista_de_numeros.sort(reverse=True)
print (f'Lista de Números ordenados: { lista_de_numeros } ' )