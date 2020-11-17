#Faça um Programa que leia uma lista de 10
#números reais e mostre-os na ordem inversa.
#OBS: Faça de duas formas, usando utilizando
#o método .reverse() e não utilizando o método
#.reverse()
lista = []
for x in range(1, 11):
    num = int(input("Digite um número: "))
    lista.append(num)
print("A lista digitada foi {}".format(lista))
lista.reverse()
print("A lista em ordem inversa foi {}".format(lista))

