#Faça um Programa que leia um vetor de 10 caracteres, 
#e diga quantas consoantes foram lidas. Imprima as consoantes.
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
num = 0
for c in range(1, 11):
    letra = input("Digite uma letra: ")
    if letra not in vogais:
        consoantes.append(letra)
        num = num + 1
print("Foram lidas {} consoantes: ".format(num))
print("As consoantes que foram lidas {} ".format(consoantes))




