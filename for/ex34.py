#Faça um programa em python que leia 2 listas de com 5 valores inteiros.
#Ao final verifique quais elementos do segundo vetor pertencem ao primeiro vetor.
#Caso não haja nenhum elemento em comum,
#o programa deve informar isso. Observe o exemplo abaixo: *
lista1= []
lista2= []
for c in range(1, 6):
    num = int(input("Digite os números da primeira lista: "))
    lista1.append(num)
for c in range(1, 6):
    num1 = int(input("Digite os números da segunda lista: "))
    lista2.append(num1)
for c in lista2:
    if c in lista1:
         print(c)
    elif c not in lista1:
        print("Não tem")
    