#Um banco concederá um crédito especial aos seus clientes,
#variável com o saldo médio no último ano. Faça um algoritmo
#que leia o saldo médio de um cliente e calcule o valor do crédito
#de acordo com a tabela abaixo. Mostre uma mensagem informando o saldo médio e o valor do crédito.
#Saldo médio	Percentual
#de 0 a 200	    nenhum crédito
#de 201 a 400	20% do valor do saldo médio
#de 401 a 600	30% do valor do saldo médio
#acima de 601	40% do valor do saldo médio
num = float(input("Digite seu saldo médio do último ano: "))
if num >= 0 and num <= 200:
    print('Seu saldo médio é R$ {:.2f}'.format(num))
    print('e somente clientes com saldos maiores que R$ 200,00 tem acesso ao crédito especial! ')
elif num > 200 and num <= 400:
    print('Seu saldo médio é de R$ {:.2f}'.format(num))
    credito = num * 20 / 100
    print('Você receberá um crédito especial de {:.2f}'.format(credito))
elif num > 400 and num <= 600:
    print('Seu saldo médio é de {:.2f}'.format(num))
    credito = num * 30 / 100
    print('Você receberá um crédito especial de {:.2f}'.format(credito))
elif num > 600:
    print('Seu saldo médio é de {:.2f}'.format(num))
    credito = num * 40 / 100
    print('Você receberá um crédito especial de {:.2f}'.format(credito))
else:
    print('Digite um número válido!')