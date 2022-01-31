nome = str(input("Insira o nome do Aluno: "))
n1 = float(input("Insira a nota da P1: "))
n2 = float(input("Insira a nota da P2: "))
m = (n1+n2) / 2
if m < 5.0:
    print("O aluno {} foi Reprovado, sua media foi {:.2f}.".format(nome, m))
elif m <= 6.9:
    print("O aluno {} esta em Recuperacao, sua media foi {:.2f}.".format(nome, m))
else:
    print("O aluno {} foi Aprovado, sua media foi {:.2f}.".format(nome, m))
