num = cont = soma = 0
while True:
    num = int(input("Digite um numero [999 para encerrar]: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Foram digitados {cont} numeros e a soma deles é {soma}.")
print("FIM")
