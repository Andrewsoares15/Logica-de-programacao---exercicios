#Faça um programa para escrever os 10 primeiros múltiplos de 3.
num = 3
while num <= 30:
    if num % 3 == 0:
        print(num)
        #print("{} é multiplo de 3".format(num))
    num = num + 3