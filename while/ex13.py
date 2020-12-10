#Faça um Programa que leia uma lista de 10
#números reais e mostre-os na ordem inversa.
#OBS: Faça de duas formas, usando utilizando
#o método .reverse() e não utilizando o método
#.reverse()
vetor = []
i = 1
while i <= 10:
    n = int(input("Digite um número:"))
    vetor.append(n)
    i += 1
i = 9
while i >= 0:
    print (vetor[i])
    i -= 1 
print(vetor) 
sorted(vetor)
vetor.reverse
(print(vetor))