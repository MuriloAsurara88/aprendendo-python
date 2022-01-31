from datetime import date
atual = date.today().year
n1 = 0
n2 = 0
for c in range(0, 7):
    nasc = int(input("Digite o ano em que a pessoa nasceu: "))
    idade = atual - nasc
    if idade < 21:
            n1 = n1 + 1
    else:
            n2 = n2 + 1
print("O numero de pessoas com 21 anos ou mais é: {}".format(n2))
print("O numero de pessoas com menos de 21 anos é: {}".format(n1))
print("FIM")
