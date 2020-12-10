#construir um programa que leia o preço
#de uma quantidade indeterminada de produtos de um mercado
#e calcule, armazene e imprima a soma de todos os preços
#Não permitir preço zero ou negativo. 
#Flag de saída: 'N' para pergunta “Deseja Continuar?”.
total = []
desejo = 'Sim'
while desejo == 'Sim':
    preço = float(input("Digite o preço do produto: "))
    if preço >= 1:
        desejo = input("Deseja continuar? Digite N para sair e Sim para continuar! ")
        total.append(preço)
    else:
        print("Digite um preço válido! ")
soma = sum(total)
print("A soma de todos os preços deu R${:.2f}".format(soma))