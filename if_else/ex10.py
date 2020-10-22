#Escreva um programa que recebe um inteiro e diga se é par
#ou ímpar.
num = int(input("Digite um número inteiro: "))
resultado = num % 2
if resultado == 0:
    print("O número {} é par".format(num))
else :
    print("O número {} é impár".format(num))