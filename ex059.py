n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print("-=-"*20)
    print('''    [1] Soma
    [2] Multiplição
    [3] Maior Valor
    [4] Novos Numeros
    [5] Sair''')
    print("-=-" * 20)
    opcao = int(input("Qual é a opcao desejada ?"))
    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} + {} é igual a {}.".format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print("A multiplicação entre {} e {} é igual a {}.".format(n1,n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("A maior valor é {}.".format(maior))
    elif opcao == 4:
        print("Informe os numeros novamente: ")
        n1 = int(input("Insira o primeiro numero: "))
        n2 = int(input("Insira o segundo numero: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção invalida. Digite novamente a sua opção.")
print("+-+" * 20)
print("FIM")
