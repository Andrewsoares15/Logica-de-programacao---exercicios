#Melhore o exercício nº 4, para calcular
#a tabuada de um intervalo de dois
#números que será informado pelo
#usuário. Esse programa deve conter uma
#função, imprimetabu, que recebe por
#parâmetro os dois números do intervalo.
#Esta função deve escrever as tabuadas
#na tela do menor para o maior. OBS:
#Atenção aos números iguais.
def tabuada(valor,valor1):
    while valor <= valor1:
        for c in range(1, 11):
            print('{} x {} = {}'.format(valor, c, valor*c))
        valor = valor + 1
num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(tabuada(num, num2))