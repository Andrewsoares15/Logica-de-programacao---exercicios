#Faça um programa para solicitar o nome e as duas notas e um aluno.
#Calcular sua média e informá-la. Se ela for inferior a 7, escrever
#"Reprovado"; caso contrário escrever "Aprovado".
nome = input("Digite seu nome")
av1= float(input("Digite sua nota da av1"))
av2= float(input("Digite sua nota da av2"))
media = (av1 + av2)/ 2
if media >= 7:
    print("{}, Sua media foi {},e voce está aprovado".format(nome, media))
else:
    print("{}, Sua media foi {}, e voce está reprovado".format(nome, media))   
