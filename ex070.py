print("*-*" * 20)
print("SUPER AZURARAO")
print("*-*" * 20)
total = total1000 = cont = menor = 0
barato = " "
while True:
    produto = str(input("Insira o nome do Produto: ")).upper()
    valor = float(input("Insira o valor do Produto: R$ "))
    total += valor
    cont += 1
    if valor > 1000:
        total1000 += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N] ?")).strip().upper()[0]
    if resp == "N":
        break
print(f"O Valor total dos produtos é: R$ {total:.2f}")
print(f"Foram comprados {total1000} produtos que custam mais que R$ 1000,00.")
print(f"O Produto mais barato é a {barato} que custa {menor:.2f}.")

print("FIM")
