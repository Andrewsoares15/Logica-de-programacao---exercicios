#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.
numero = []
pares= []
impares = []
for c in range (1, 21):
    num = int(input("Digite um número: "))
    numero.append(num)
    if num % 2 == 0:
        pares.append(num)
    else :
        impares.append(num)
print("Os números digitados foram {}".format(numero))
print("Os números pares foram {} ".format(pares))
print("Os números impares foram {}".format(impares))




