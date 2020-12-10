#Escreva uma função que receba uma palavra
#como parâmetro e retorne a quantidade de
#vezes que a letra b aparece. 
def verifica(valor):
    return 'A letra b apareceu {} vezes'.format(valor.count('b'))
palavra = input("Digite uma palavra: ")
print(verifica(palavra))