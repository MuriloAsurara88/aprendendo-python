from random import randint
print("=-="*10)
print("VAMOS JOGAR PAR OU IMPAR ?")
print("=-="*10)
vitoria = 0
while True:
    jog = int(input("Diga um valor? "))
    cpu = randint(0, 10)
    result = jog + cpu
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Voce escolhe PAR ou IMPAR [P/I] ?")).strip().upper()[0]
    print(f"Voce jogou {jog} e o computador jogou {cpu}. Total é {result}.")
    print("DEU PAR." if result % 2 == 0 else "DEU IMPAR.")
    if escolha == "P":
        if result % 2 == 0:
            print("Voce Venceu! Parabens!")
            vitoria += 1
        else:
            print("Voce Perdeu!")
            break
    elif escolha == "I":
        if result % 2 == 1:
            print("Voce Venceu! Parabens!")
            vitoria += 1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar novamente!")
print(f"Voce venceu {vitoria} partida(s) seguidas!")