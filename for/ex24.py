#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for c in range(1, 11):
    num = int(input("Digite um número: "))
    lista.append(num)
lista.reverse()
print(lista)
