#Crie um programa para ler a matrícula, o nome e o salário
#de dois empregados. Descontar 5% no salário do primeiro
#e acrescentar 9% no salário do segundo. Informar:
#o valor do desconto do primeiro; o valor do acréscimo do segundo;
#o salário final do primeiro; o salário final do segundo
nome = []
salario = []
matricula = []
for c in range(1, 3):
    name = input("Digite seu nome: ")
    nome.append(name)
    sal = float(input("Digite seu salário: "))
    salario.append(sal)
    matri = int(input("Digite o número da sua matrícula: "))
    matricula.append(matri)
desconto = salario[0] *5 / 100
new_salario = salario[0] - desconto
acrescimo = salario[1] *9 / 100
novo_salario = acrescimo + salario[1]
print("{}, matricula: {}, salario R${:.2f}, valor do desconto {:.2f} ".format(nome[0], matricula[0], salario[0],desconto))
print("Sr {}, seu novo salário é de R${:.2f}".format(nome[0], new_salario))
print("{}, matricula: {}, salário R$ {:.2f}, valor do acrescimo {:.2f}".format(nome[1], matricula[1], salario[1],acrescimo ))
print("Sr {}, seu novo salário é de R${:.2f} ".format(nome[1], novo_salario))