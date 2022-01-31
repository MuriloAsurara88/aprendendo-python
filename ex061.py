primeiro = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razao da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} ".format(termo), end=" ")
    termo += razao
    cont += 1
print("FIM")
