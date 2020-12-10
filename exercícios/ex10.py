#Faça um programa para solicitar o nome e o salário de um empregado.
#Calcular e descontar 8% do seu salário.
#Informar o valor do desconto e o salário líquido a receber
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
desconto = salario * 8 / 100
novo_salario = salario - desconto
print("Senhor {}, foi descontado de seu salário {:.2f} e você receberá {:.2f}".format(nome, desconto, novo_salario))