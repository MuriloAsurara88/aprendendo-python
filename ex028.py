import random
num = int(input("Escolha um numero de 0 a 5: "))
n1 = random.randrange(0, 5)
if num == n1:
    print("O numero escolhido foi {}, Acertou miseravi !".format(num))
else:
    print("O numero escolhido foi {}, Errou seu Zé ruela !".format(num))

print("O Numero secreto é: {}.".format(n1))
