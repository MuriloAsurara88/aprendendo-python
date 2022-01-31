frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A letra A apareceu primeiro na posição {}.".format(frase.find("A")+1))
print("A letra A apareceu por ultimo na posição {}.".format(frase.rfind("A")+1))

