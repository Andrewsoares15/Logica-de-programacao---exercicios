#João Papo-de-Pescador, homem de bem, comprou um
#microcomputador para controlar o rendimento diário de seu
#trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do estado de São Paulo
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na
#variável excesso a quantidade de quilos além do limite e na
#variável multa o valor da multa que João deverá pagar. Imprima os
#dados do programa com as mensagens adequadas
peso = float(input("Informe o peso dos peixes pesacados: "))
peso_max = 50
multa = 4
if peso > peso_max :
    print("O Peso máximo diário permitido é 50kg! ")
    print("A cada kg excedido do valor máximo, pagará uma multa de 4 Reais")
    excesso= peso - peso_max
    multa = excesso * 4
    print("Valor da multa por excesso R${:.2f}".format(multa))