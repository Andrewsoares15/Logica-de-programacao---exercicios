#Escreva um programa que leia a quantidade
#de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundo.
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
min = int(input("Digite a quantidade de minutos: "))
seg = int(input("Digite a quantidade de segundos: "))
seg1 = dias * 86400
seg2 = horas * 3600
seg3 = min * 60
total = (seg1 + seg2) + (seg3 + seg)
print("O total em segundos é {}".format(total))
