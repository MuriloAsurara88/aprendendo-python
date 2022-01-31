from datetime import date
atual = date.today().year
ano = int(input("Qual o ano de nascimento: "))
idade = atual - ano
print("=-="*20)
print("Voce tem {} anos.".format(idade))
if idade <= 9:
    print("Sua categoria e a MIRIM.")
elif idade < 15:
    print("Sua categoria e a INFANTIL.")
elif idade < 20:
    print("Sua categoria e a JUNIOR.")
elif idade < 25:
    print("Sua categoria e a SENIOR.")
else:
    print("Sua categoria e a MASTER.")
