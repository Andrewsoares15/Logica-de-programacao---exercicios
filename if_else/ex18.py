#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ['a', 'e', 'i', 'o', 'u', ]
letra = input("Digite uma letra: ")
if letra not in vogais:
    print("Você digitou a letra '{}', ela é uma consoante!".format(letra))
else:
    print("Você digitou a letra '{}', ela é uma vogal!".format(letra))
