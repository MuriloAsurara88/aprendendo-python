cond = "S"
maior = menor = soma = qtd = media = 0
while cond in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cond = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
media = soma / qtd
print("Voce digitou {} numeros e a media entre eles é {:.2f}.".format(qtd, media))
print("O maior valor digitado {} e o menor valor foi {}.".format(maior, menor))
print("FIM")
