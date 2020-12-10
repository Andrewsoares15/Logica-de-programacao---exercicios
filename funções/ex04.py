#Desenvolva um programa que
#apresente a tabuada de 0 até 10
#para um número determinado pelo
#usuário. Esse programa deve conter
#uma função imprime_tabu que recebe
#por parâmetro o número digitado
#pelo usuário e escreve a tabuada na
#tela.
def tabuada(valor):
    for c in range(1, 11):
         print('{} x {} = {}'.format(valor, c, valor*c))
num = int(input("Digite um número: "))
print(tabuada(num))


