#Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números,/
#  o algoritmo deve escrever esses 20 números lidos na ordem inversa.

numeros = [int(input("Número: ")) for x in range(20)]
print(numeros)
Listainvertida = [num for num in reversed(numeros)]
print(Listainvertida)
  