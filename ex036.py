nome = str(input("Insira o seu nome: "))
vcasa = float(input("Insira o valor do imovel para financiamento: "))
sal = float(input("Insira o seu salario bruto em R$: "))
tpag = int(input("Insira em quantos meses deseja pagar: "))
prest = vcasa / tpag
minimo = sal * 30 / 100
if prest <= minimo:
    print(40 * "=-")
    print("O emprestimo foi Aprovado valor das prestacoes sera de R$ {:.2f}.".format(prest))
    print(40 * "=-")
else:
    print(40 * "=-")
    print("O valor das prestacoes excede a margem de 30% do salario. Infelizmente o financiamento nao foi Aprovado.")
print( 40 * "=-")
print("Obrigado por procurar a BOX FINANCIAL, tenha um bom dia Sr.{}.".format(nome))
print( 40 * "=-")
