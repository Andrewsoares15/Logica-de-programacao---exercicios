#Faça um programa que leia duas listas com 10
#elementos cada. Gere uma terceira lista de 20
#elementos, cujos valores deverão ser compostos
#pelos elementos intercalados das duas outras listas...
def intercala(L,L2):
    intercalada = []
    for a,b in zip(L, L2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada
lista1 = [10, 9, 8, 7, 6, 5 , 4, 3, 2, 1]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = intercala(lista1, lista2)
print("Lista1: {}" .format(lista1))
print("Lista2: {}" .format(lista2))
print("Lista Intercalada: {}".format(lista))
