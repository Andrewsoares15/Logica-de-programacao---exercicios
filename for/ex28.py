#Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.
from functools import reduce

numeros = []
for c in range(1, 6):
    num = int(input("Digite um número: "))
    numeros.append(num)
soma = sum(numeros)
print("O cálculo entre os números é {}".format(soma))
multiplicação = reduce(lambda x, y: x * y,(numeros))
print("A multiplicação entre os números foi {}".format(multiplicação))
print("Os números digitados foram {}".format(numeros))
