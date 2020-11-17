#Faça um programa que verifique se um valor inteiro digitado pelo usuário
#é positivo, negativo ou igual a zero.
def verifica(valor):
    if valor > 0 :
        print("O valor {} é positivo".format(valor))
    elif valor < 0:
        print("O valor {} é negativo".format(valor))
    else:
        print("O número digitado é igual a 0")
num = int(input("Digite um número: "))
print(verifica(num))