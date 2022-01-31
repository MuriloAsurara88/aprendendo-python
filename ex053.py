frase = str(input("Digite a frase que deseja analisa: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("o inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo.")
else:
    print("Não é um palindromo.")

