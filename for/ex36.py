#Faça programa que solicite a idade de 250 pessoas.
#No final mostre o total de pessoas com menos de 18 anos
#o total de pessoas com mais de 65 anos e a menor idade lida. 
menoresde_18 = []
idosos = []
for c in range(1 , 251):
    idade= int(input("Digite sua idade: "))
    if idade < 18:
        menoresde_18.append(idade)
    elif idade > 65:
        idosos.append(idade)
total_jovens = len(menoresde_18)
total_idosos = len(idosos)
print("O total de menores de 18 é: {}".format(total_jovens))
print("O total de maiores de 65 é: {}".format(total_idosos))
print("A menor idade lida foi {}".format(min(menoresde_18)))

