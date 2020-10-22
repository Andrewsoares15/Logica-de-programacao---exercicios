#Faça um programa para solicitar o código, a quantidade de alunos do
#sexo masculino, a quantidade de alunos do sexo feminino e a quantidade
#de alunos aprovados de uma determinada turma. Calcular e informar: a
#porcentagem de alunos do sexo masculino; a porcentagem de alunos do
#sexo feminino; a porcentagem de alunos reprovados; o total de alunos da
#turma.
aluno_mas = int(input("Digite a quantidade de alunos masculinos: "))
aluno_fem = int(input("Digite a quantidade de alunos femininos: "))
aprov = int(input("Digite a quantidade de alunos aprovados: "))
total = aluno_mas + aluno_fem
porc_Mas =  aluno_mas*100/total
porc_fem = aluno_fem*100/total
reprov = total - aprov
print("A porcentagem de alunos do sexo masculino é {:.2f} %".format(porc_Mas))
print("A porcentagem de alunos do sexo feminino é {:.2f} %".format(porc_fem))
print("A porcentagem de alunos reprovados é {:.2f} %".format(reprov))
print("O total de alunos é {:.2f} %".format(total))