#Elabore um programa para solicitar o nome, o sexo e o
#salário bruto de um empregado. Se o seu sexo for masculino,
#descontar 5% de seu salário; caso contrário, descontar 3%.
#Informar o valor do desconto e o salário líquido.
nome = input("Digite seu nome: ")
sexo = input("Digite F para feminino e M para masculino ")
salario = float(input("Digite seu salário: "))
if sexo == 'M' :
    porc_M = salario*5 /100
    desconto = salario - porc_M
    print("desconto de {}, seu salário liquido é {}".format(porc_M, desconto))
else :
    porc_F= salario*3 / 100
    descontof = salario - porc_F
    print("desconto de {}, seu salário liquido é {}".format(porc_F, descontof))