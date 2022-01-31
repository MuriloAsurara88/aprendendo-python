dist = float(input("Digite a distância da viagem em Km: "))
if dist <= 200:
    kilom = dist * 0.5
    print("O valor da passagem é: {:.2f} .".format(kilom))
else:
    kilom = dist * 0.45
    print("O valor da passagem é: {:.2f} R$.".format(kilom))

