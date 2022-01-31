soma = 0
media = 0
maiorhomem = 0
nomevelho = 0
totmulher = 0
for c in range(1, 5):
    print("=-" * 15)
    nome = str(input("Insira o nome da {}ª pessoa: ".format(c))).upper()
    idade = int(input("Insira a idade da pessoa: "))
    sexo = str(input("Insira o sexo da pessoa [F/M]: ")).strip().upper()
    soma += idade
    if c == 1 and sexo in "Mm":
        maiorhomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher += 1
media = soma/4
print("A Media de idade do grupo é de: {}".format(media))
print("O homem mais velho se chama {}, e tem {}".format(nomevelho, maiorhomem))
print("No grupo existem {} mulheres, com menos de 20 anos.".format(totmulher))
print("FIM DA ANALISE")
