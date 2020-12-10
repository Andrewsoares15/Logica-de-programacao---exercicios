#Crie um programa onde o usuário digite três valores e
#imprima na tela o maior valor, devendo para isso, criar
#uma função Maior que retorne o maior dos três valores ou
#uma mensagem dizendo que os números são iguais.
def valores(valor1, valor2, valor3):
    if valor1 > valor2 and valor1> valor3:
        return 'O {} é o maior número'.format(valor1)
    elif valor2 > valor1 and valor2 > valor3:
        return 'O {} é o maior número'.format(valor2)
    elif valor3 > valor1 and valor3 > valor2:
        return 'O {} é o maior número'.format(valor3)
    else:
        return 'Os números são iguais'
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite um número: "))
valor3 = int(input("Digite um número: "))
print((valores(valor1, valor2, valor3)))