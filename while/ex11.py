#construir um programa que leia um número inteiro
#e imprima todos os números ímpares entre 1 e o número lido.
num = 1
while num >= 1:
    num = int(input("Digite um número: "))
    soma = list(range(1, num, 2))   
    print("Os números pares entre o 1 e o número digitado são {}".format(soma))




