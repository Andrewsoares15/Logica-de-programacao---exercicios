#Escreva um programa que pergunte o depósito inicial e a taxa de juros de
#uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no período.
#8. Altere o programa anterior de forma a perguntar também o valor
#depositado mensalmente. Esse valor será depositado no início de cada mês, e
#você deve considerá-lo para o cálculo de juros do mês seguinte.
depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal:"))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo-depósito))