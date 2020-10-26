#Melhore o programa da tabuada utilizando o while.
#Modifique a tabuada para que o usuário possa
#escolher o início e o fim, ao invés de começar com 1 e
#ir até 10.

n = int(input("Tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))
while inicio <= fim:
    print('{} x {} = {}'.format(n, inicio, (n * inicio)))
    inicio = inicio + 1