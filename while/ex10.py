#construir um programa que leia o sexo
#de uma quantidade indeterminada de pessoas e calcule,
#aporcentagem de pessoas dormazene e imprima o total de pessoas, a  sexo masculino
#e a porcentagem de pessoas do sexo feminino. 
#Flag de saída: sexo diferente de “M” e “F”.
sexo = []
masculino = []
feminino = []
genero = 'F'
while genero == 'F' or genero == 'M':
    genero = input("M para masculino e F para feminino! Digite seu Sexo: ")
    if genero == 'F' or genero == 'M':
        sexo.append(genero)
    if genero == 'F':
        feminino.append(genero)
    if genero == 'M':
        masculino.append(genero)
total = len(sexo)
total_masculino = len(masculino)
total_feminino = len(feminino)
porcentagem_M = total_masculino *100/ total
porcentagem_F = total_feminino * 100 / total
print("O total de pessoas é {}!".format(total))
print("A porcentagem de alunos(M) é {:.2f}%".format(porcentagem_M))
print("A porcentagem de alunas é {:.2f}%".format(porcentagem_F))