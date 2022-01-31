print("Bom dia, Vamos calcular os ajustes salariais dos funcíonarios.")
sal = float(input("Digite o Valor do Salario em R$: "))
if sal <= 2500.00:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print("Seu salário atual é de {:.2f} R$. No próximo mês seu salário será de {:.2f} R$.".format(sal, nsal))
