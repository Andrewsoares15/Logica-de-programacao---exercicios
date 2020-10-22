#Crie um programa para solicitar o ano atual e o ano de
#nascimento de uma pessoa. Calcular sua idade aproximada e exibir a seguinte
#mensagem:
ano= int(input("Digite o ano atual: "))
ano_nas= int(input("Digite o ano de nascimento"))
idade = ano - ano_nas
if idade <16:
    print("Não eleitor")
elif idade >=18 and idade <=65:
    print("Eleitor obrigatorio")
elif idade > 65:
    print("Eleitor facultativo")

        