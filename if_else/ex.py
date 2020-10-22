#Faça um programa que leia dois números e mostre qual o
#maior dos dois. O programa deve informar caso sejam iguais.
n1= int(input("Digite um número: "))
n2= int(input("Digite outro número: "))
if n1 > n2 :
    print("{} é o número maior! ".format(n1))
elif n1 < n2 :
    print("{} é o número maior!" .format(n2))
else:
    print("Os números {} e {} são iguais! ".format(n1, n2))