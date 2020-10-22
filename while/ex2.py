from pip._vendor.distlib.compat import raw_input

loop = True
lista = []

while(loop):
    numero = float(raw_input('digite um numero inteiro: '))
    if numero != 0:
        lista.append(numero)
    else:
        loop = False

print('A quantidade de valores digitados é de', len(lista))
print('Soma é de', sum(lista))
print('Média é de', round(sum(lista) / len(lista), 2))