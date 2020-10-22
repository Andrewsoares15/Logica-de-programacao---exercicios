#Crie um programa para ler o valor do salário mínimo, o
#nome e o salário bruto de um empregado. Se o seu salário for
#menor que um salário mínimo descontar 2%; se for igual,
#descontar 5%, e se for superior, descontar 8%. Informar o
#valor do desconto e o salário líquido.3

salario_min = float(input("Digite o valor do salário mínimo atual: "))
nome = input("Digite seu nome: ")
salario_bruto = float(input("Digite seu salário bruto: "))
if salario_bruto < salario_min:
    desconto = salario_bruto*2/100
    novo_salario = salario_bruto - desconto
    print("O valor do desconto foi {} e seu salário liquido é {}".format(desconto, novo_salario))
elif salario_bruto == salario_min :
    desconto2 = salario_bruto*5/100
    novo2_salario = salario_bruto - desconto2
    print("Seu desconto foi de {} e seu salário liquido é {}".format(desconto2, novo2_salario))
elif salario_bruto > salario_min :
    desconto3 = salario_bruto*8/100
    novo3_salario = salario_bruto - desconto3
    print("Seu desconto foi de {} e seu novo salário é de {}".format(desconto3, novo3_salario))