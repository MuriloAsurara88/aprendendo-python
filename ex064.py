n = cont = soma = 0
n = int(input("Digite um numero [999 para encerrar]: "))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input("Digite um numero [999 para encerrar]: "))
print("Foram digitados {} e a soma dos numeros digitados é {}.".format(cont, soma))
print("FIM")