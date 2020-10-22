#Faça um programa que calcule o aumento de um
#salário. Ele deve solicitar o valor do salários e a
#porcentagem do aumento. Exiba o valor do aumento e
#do novo salário.
salario = float(input("Digite o valor do salario: "))
aumento = float(input("Digite a porcentagem do aumento: "))
novo_salario = salario*aumento/100
salario_novo = salario + novo_salario
print("seu salário é R${:.2f}, com o aumento de {:.2f} %, você recebera a mais cerca de R${:.2f},\n e ganhara um total de R${:.2f}".format(salario, aumento, novo_salario, salario_novo))