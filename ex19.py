#Faça um programa que armazene cinco valores inteiros
#digitados pelo usuário em uma lista. Ao final, o programa
#deve informar:
#os valores da lista
#a quantidade de ocorrências do número 9
#a posição (ou posições) da lista em que o número 3 aparece
#os valores pares da lista  
num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
num4 = int(input("Digite outro número: "))
num5 = int(input("Digite outro número: "))
numero = [num, num2, num3, num4, num5]
print("você digitou os seguintes valores: {}".format(numero))
print("Os valores pares digitados foram: ")
pares = []
for c in numero:
    if c % 2 == 0:
        pares.append(c)
print("números pares: {}".format(pares))
print("O valor 3 apareceu na: {}º posição".format(numero.index(3)))
print("O número 9 apareceu {} vezes".format(numero.count(9)))