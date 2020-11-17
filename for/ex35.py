#Faça um Programa que leia uma lista de 10
#caracteres, e diga quantas consoantes foram lidas.
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
letras = []
for x in range(1 , 11):
    digite = input("Digite uma letra: ")
    letras.append(digite)
    if digite not in vogais:
        consoantes.append(digite)
print("As letras digitadas foram {}".format(letras))
print("As consoantes digitadas foram {}".format(consoantes))
print("O total de consoante foi {}".format(len(consoantes)))
