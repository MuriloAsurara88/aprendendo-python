import calendar
ano = int(input("Digite o ano desejado: "))
if calendar.isleap(ano):
    print("O Ano {} é Bissexto!".format(ano))
else:
    print("O Ano {} não é Bissexto!".format(ano))
