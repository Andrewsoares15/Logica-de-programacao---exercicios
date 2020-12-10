#Jogo de Pedra, papel e tesoura: nesse jogo cada jogador faz sua escolha
#1 –Tesoura, 2 – Pedra, 3 – Papel,
#e vence aquele que escolher um objeto que seja capaz de vencer o outro:
#•	Tesoura corta papel
#•	Pedra quebra tesoura
#•	Papel embrulha a pedra
jogador1= input("Escolha pedra, papel ou tesoura: ")
jogador2= input("Escolha pedra, papel ou tesoura: ")   
if jogador1 == 'pedra' and jogador2 == 'tesoura':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Pedra quebra a tesoura, primeiro jogador ganhou!")
elif jogador1 == 'tesoura' and jogador2 == 'papel':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Tesoura corta o papel, o primeiro jogador ganhou! ")
elif jogador1 == 'papel' and jogador2 == 'pedra':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Papel embrulha a pedra, o primeiro jogador venceu!")
elif jogador2 == 'pedra' and jogador1 == 'tesoura':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Pedra quebra a tesoura, primeiro jogador ganhou!")
elif jogador2 == 'tesoura' and jogador1 == 'papel':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Tesoura corta o papel, o primeiro jogador ganhou! ")
elif jogador2 == 'papel' and jogador1 == 'pedra':
    print("O primeiro jogador escolheu {} e o segundo escolheu {}".format(jogador1, jogador2))
    print("Papel embrulha a pedra, o primeiro jogador venceu!")
else:
    print("Faça escolhas válidas!")

    

