s = 0
cont = 0
for n in range(1, 7):
    num = int(input("Digite o numero {}º valor : ".format(n)))
    if num % 2 == 0:
        s += num
        cont = cont + 1
print("Voce informou {} numeros PARES e a soma dos numeros pares é: {}".format(cont, s))
print("FIM")
