#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
lista = []
for c in range(1, 6):
    num = int(input("Digite um número: "))
    lista.append(num)
print("Os números digitados foram: {}".format(lista))