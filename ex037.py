n = int(input("Digite um numero inteiro: "))
print(""" Escolha uma das bases para conversao: 
[ 1 ] converte para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opcao e: "))
if opcao == 1 :
    print("{} convertido para BINARIO e: {} .".format(n, bin(n)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL e: {} .".format(n, oct(n)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL e: {} .".format(n, hex(n)[2:]))
else:
    print("Opcao Invalida")
