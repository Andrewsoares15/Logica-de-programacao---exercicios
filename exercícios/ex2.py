#Faça um programa que leia dois valores inteiros e ao final informe a soma, a
#subtração, a multiplicação e a divisão dos dois números.
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
print("A soma entre eles é {}".format(soma))
print("A subtração entre eles é {}".format(sub))
print("A multiplicação entre eles é {}".format(mult))
print("A divisão entre eles é {}".format(div))