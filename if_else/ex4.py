#Faça um programa para solicitar o nome e a idade de uma pessoa.
#Se sua idade for menor que 18 anos, escrever a mensagem: "É menor
#".
nome = (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
if (idade < 18):
    print(nome, "Voce é menorr de idade")
else:
    print(nome, "Você é maior de idade")
    