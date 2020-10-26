#Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita)
# e desconto de 10% do INSS.
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, valor do salário bruto, valor dos descontos
# sindicato, inss, imposto de renda e o total deles. valor do FGTS e seu
#salário líquido com todos os descontos.


valor_horas = float(input("Digite o valor da sua hora trabalhada: "))
quanti_horas = int(input("Digite a quantidade de horas trabalhadas: "))
salario = quanti_horas * valor_horas
if salario <=900 :
    print("Seu salário bruto é {:.2f}".format(salario))
    sindicato =(salario*3/100) #desconto do sindicato
    print("Descnto do sindicato R$ {:.2f}".format(sindicato))
    fgts = (salario*11/100)
    print("Valor do FGTS {:.2f}".format(fgts))
    inss =(salario*10/100) #desconto do INSS
    print("Desconto do inss {:.2f}".format(inss))
    total = sindicato + inss
    print("O total de desconto foi {:.2f}".format(total))
    novo_salario= salario - total
    print("Salário líquido {:.2f}".format(novo_salario))
elif salario > 900 and salario <= 1500:
    print("salário bruto {:.2f}".format(salario))
    imposto_renda = salario*5/100
    print("Desconto do IR {:.2f}".format(imposto_renda))
    sindicato = salario*3/100
    print("Desconto do sindicato {:.2f}".format(sindicato))
    fgts = salario*11/100
    print("Valor do fgts {:.2f}".format(fgts))
    inss = salario*10/100
    print("Desconto do inss {:.2f}".format(inss))
    total = imposto_renda + sindicato + inss
    print("O total de descontos é {:.2f}".format(total))
    novo_salario = salario - total
    print("Seu novo salário é R${:.2f}".format(novo_salario))
elif salario > 1500 and salario <=2500:
    print("Seu salário bruto é R${:.2f}".format(salario))
    imposto_renda = salario*10/100
    print("O desconto de imposto de renda é {:.2f}".format(imposto_renda))
    sindicato = salario*3/100
    print("Desconto do sindicato {:.2f}".format(sindicato))
    fgts = salario*11/100
    print("O valor do fgts é de R${:.2f}".format(fgts))
    inss = salario*10/100
    print("O valor do desconto do inss é {:.2f}".format(inss))
    total = imposto_renda + sindicato + inss
    print("O total de descontos é {:.2f}".format(total))
    novo_salario = salario - total
    print("Seu salário líquido é de R${:.2f}".format(novo_salario))
elif salario > 2500:
    print("Seu sálario bruto R${:.2f}".format(salario))
    imposto_renda = salario*20/100
    print("Desconto do imposto de renda é de: {:.2f}".format(imposto_renda))
    sindicato = salario*3/100
    print("Desconto do sindicato é de: {:.2f}".format(sindicato))
    fgts = salario*11/100
    print("O valor do fgts é de: {:.2f}".format(fgts))
    inss = salario*10/100
    print("O valor do desconto do inss é de: {:.2f}".format(inss))
    total = imposto_renda + sindicato + inss
    print("O total de desconto é R${:.2f}".format(total))
    novo_salario = salario - total
    print("Seu salário líquido é de R${}".format(novo_salario))

