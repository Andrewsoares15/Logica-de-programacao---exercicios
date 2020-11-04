#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
num = 0
for c in range(1, 5):
    num = int(input("Digite suas 4 notas: "))
    notas.append(num)
print("Suas notas foram: {}".format(notas))
f = sum(notas)/4
print("Sua média foi: {} ".format(f))

