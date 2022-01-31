maior18 = 0
totalmasc = 0
totalfem = 0
while True:
        idade = int(input("Insira a idade: "))
        sexo = " "
        while sexo not in "MF":
            sexo = str(input("Insira o sexo [M/F]: ")).strip().upper()[0]
        if idade >= 18:
            maior18 += 1
        if sexo == "M":
            totalmasc += 1
        if sexo == "F" and idade < 20:
            totalfem += 1
        resp = " "
        while resp not in "SN":
            resp = str(input("Quer continuar [S/N] ?")).strip().upper()[0]
        if resp == "N":
            break
print("=-="*25)
print(f"Foram cadastrados {totalmasc} homens.")
print(f"{maior18} pessoas são maiores que 18 anos.")
print(f"Total de mulheres cadastradas com menos de 20 anos e {totalfem}.")
print("=-="*25)
print("FIM")


