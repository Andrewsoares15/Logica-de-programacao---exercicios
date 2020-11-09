#Faça um programa que receba quatro
#números inteiros e positivos do usuário e
#calcule a soma somente dos números pares
#digitados, caso o usuário tenha digitado
#somente ímpares, informe-o. OBS: SEM
#USAR ESTRUTRA DE REPETIÇÃO.
num1 = int(input("Digite um número positivo: "))
num2 = int(input("Digite outro número positivo: "))
num3 = int(input("Digite outro número positivo: "))
num4 = int(input("Digite outro número positivo: "))
numeros = [num1, num2, num3, num4]
pares = []
if num1 % 2 == 0:
    pares.append(num1)
if num2 % 2 == 0:
    pares.append(num2)
if num3 % 2 == 0:
    pares.append(num3)
if num4 % 2 == 0:
    pares.append(num4)
else:
    print("Digite somente números pares!")
soma = sum(pares)
print("A soma dos números pares foram {} ".format(soma))

    
