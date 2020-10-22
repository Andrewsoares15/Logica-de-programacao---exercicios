#Faça um programa para solicitar o nome e as duas notas e um aluno.
#Calcular sua média e informá-la. Se ela for inferior a 7, escrever
#"Reprovado"; caso contrário escrever "Aprovado".
nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua outra nota: "))
media = (nota1 + nota2) / 2
if media < 7 :
    print("{}, você está reprovado!".format(nome))
else :
    print("{}, você está aprovado! sua média foi {} ".format(nome, media))