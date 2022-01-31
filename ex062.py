print("-*-" * 5)
print("Gerador de PA")
print("-*-" * 5)
primeiro = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razao da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} ".format(termo), end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce qer visualizar a mais ? "))
print("-*-" * 5)
print("Foram mostrados {} termos dessa progressão !".format(total))
print("-*-" * 5)
print("PA FINALIZADA")
print("-*-" * 5)
