#Criar uma função que receba um caractere como
#parâmetro e retorne uma mensagem informando se
#o caracter digitado é uma vogal ou uma consoante.
def verifica(valor):
    vogal = ['a', 'e', 'i', 'o', 'u']
    if valor not in vogal:
        return 'É consoante!'
    else:
        return 'É vogal!'
letra = input("Digite uma letra: ")
print(verifica(letra))