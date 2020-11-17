def area(valor1, valor2):
    return valor1 * valor2
print('-' * 60)
print('Controle de terreno')
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento: "))
print("A área do terreno é {}".format(area(largura, comprimento)))