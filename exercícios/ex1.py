#Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado pelo usuário, assim como a
#quantidade de dias pelos quais o carro foi alugado. Calcule o
#preço a pagar, sabendo que o carro custa R$60,00 por dia e
#R$0,15 por km rodado.
km = float(input("Distância percorrida: "))
dias = int(input("Quantidade de dias que permaneceu com o carro: "))
valor = (km * 0.15) + (dias * 60) # no 0.15 não pode ser virgula, somente o ponto final
print("O total a ser pago será {:.2f}".format(valor))