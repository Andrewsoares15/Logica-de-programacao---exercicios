#Crie um programa para ler dois números e informar
#a média aritmética e a metade da diferença entre eles.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
media = (num1 + num2) / 2
if num1 > num2:
    diferença = (num1 - num2) / 2
else:
    diferença = (num2 - num1) / 2
print("A media entre eles é {}".format(media))
print("A metade da diferença entre eles é: {:.1f}".format(diferença))

