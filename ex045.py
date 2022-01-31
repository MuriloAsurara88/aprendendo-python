from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''JO KEN PO !!!)
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("QUAL SUA ESCOLHA: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!!")
sleep(1)
print("+-"*14)
print("O Computador escolheu {}.".format(itens[comp]))
print("+-"*14)
print("Voce escolheu {}.".format(itens[jogador]))
print("+-"*14)
if comp == 0:
    if jogador == 0:
        print("# EMPATE #")
    elif jogador == 1:
        print("VOCE VENCEU. PARABENS !!!")
    elif jogador == 2:
        print("VOCE PERDEU !")
    else:
        print("JOGADA INVALIDA. TENTE NOVAMENTE !")
elif comp == 1:
    if jogador == 0:
        print("VOCE PERDEU !")
    elif jogador == 1:
        print("# EMPATE #")
    elif jogador == 2:
        print("VOCE VENCEU. PARABENS !!!")
    else:
        print("JOGADA INVALIDA. TENTE NOVAMENTE !")
elif comp == 2:
    if jogador == 0:
        print("VOCE VENCEU. PARABENS !!!")
    elif jogador == 1:
        print("VOCE PERDEU !")
    elif jogador == 2:
        print("# EMPATE #")
    else:
        print("JOGADA INVALIDA. TENTE NOVAMENTE !")
print("+-"*14)
