#Faça um Programa que peça a idade e a altura de 5 pessoas,
#armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []
for c in range(1, 6):
    id = int(input("Digite sua idade: "))
    idade.append(id)
    alt = int(input("Digite sua altura: "))
    altura.append(alt)
print("As alturas digitados foram {:.2f}".format(altura))
print("As idades digitadas foram {}".format(idade))