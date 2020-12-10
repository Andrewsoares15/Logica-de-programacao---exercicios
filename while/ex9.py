#construir um programa que leia uma quantidade
#indeterminada de números e calcule, armazene e imprima a soma de todos
#os números lidos. Flag de saída: número negativo
num = 0
numeros = []
while num >= 0:  
    num = int(input("Digite um número positivo: "))    
    if num >= 0:
        numeros.append(num)
print(numeros)
soma = sum(numeros)
print("A soma de todos os números é {}".format(soma))