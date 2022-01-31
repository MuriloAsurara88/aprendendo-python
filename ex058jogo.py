from random import randint
cpu = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um numero entre 0 e 10.")
print("Sera que voce consegue advinhar?")
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite ?"))
    tentativas += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print("Mais...Tente mais uma vez.")
        elif jogador > cpu:
            print("Menos...Tente outra vez.")
print("Acertou com {} tentativas, Parabens BOXEXUDO !".format(tentativas))
print("FIM DE JOGO")
