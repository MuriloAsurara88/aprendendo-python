print("LOJAS ASURARA")
preco = float(input("Qual o valor da compra: R$ "))
print('''FORMAS DE PAGAMENTO)
[ 1 ] - A Vista em Dinheiro ou Cheque
[ 2 ] - A Vista no cartao
[ 3 ] - 2x no Cartao
[ 4 ] - 3x ou mais no Cartao''')
opcao = int(input("Qual a opcao de pagamento desejada ? "))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra sera parcelada em 2 vezes de R$ {:.2f} .".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    tparc = int(input("Quantas parcelas"))
    parcela = total / tparc
    print("Sua compra sera parcela em {} de R$ {:.2f}.".format(tparc, parcela))
else:
    total = preco
    print("Forma de pagamento invalida. Tente novamente.")
print("Total a pagar pela compra: R$ {:.2f}.".format(total))
