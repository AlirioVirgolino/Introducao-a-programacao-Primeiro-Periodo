#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
#Imprima o resultado da soma de todos os valores da matriz no terminal;


from random import randint

a = []

for linha in range(10):
    linha = []
    for coluna in range(10):
        linha.append(randint(0, 10))
    a.append(linha)
    print(a)
soma = list(map(sum, a))
print(soma)
somafinal = sum(soma)
print(somafinal)

   