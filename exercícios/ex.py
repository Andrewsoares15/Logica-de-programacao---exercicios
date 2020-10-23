#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para viagemm#
dist = float(input("Qual distância a ser percorrida"))
vm = float(input("Digite a velocidade média"))
tempo= dist / vm 
print("O tempor em horas será de {:.2f} ".format(tempo) )
