#Considere a lista V=[9, 8, 7, 12, 0, 13, 21].
#Faça um programa que copie para P os
#números pares e para I os números ímpares.
V = [9, 8, 7, 12, 0, 13, 21]
pares = []
impares = []
for x in V:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print("Os números pares são {}".format(pares))
print("Os números impares são {}".format(impares))
