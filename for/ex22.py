#Faça um programa que armazene cinco valores inteiros
#digitados pelo usuário em uma lista. Ao final, o programa
#deve informar:
#os valores da lista
#a quantidade de ocorrências do número 9
#a posição (ou posições) da lista em que o número 3 aparece
#os valores pares da lista
lista = []
pares = []
for c in range (1, 6):
    valor = int(input("Digite um número: "))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
        
print("Os valores digitados foram: {}".format(lista))
print("Os valores pares digitados foram: {}".format(pares))
lista.pop(1)
lista.insert(2, 3)
print("O valor 3 apareceu na {}º posição ".format(lista.index(3)))
print("O valor 9 apareceu {} vezes ".format(lista.count(9)))