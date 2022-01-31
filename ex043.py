print("=+=" * 20)
print("CALCULANDO IMC")
print("=+=" * 20)
peso = float(input("Por favor insira seu peso em Kg: "))
altura = float(input("Por favor insira sua altura em metros: "))
imc = peso / (altura*altura)
if imc < 18.5:
    print("Seu IMC e {}. Voce esta abaixo do peso ideal.".format(imc))
elif imc < 25:
    print("Seu IMC e {}. Voce esta com o peso ideal.".format(imc))
elif imc < 30:
    print("Seu IMC e {}. Voce esta com sobrepeso.".format(imc))
elif imc < 40:
    print("Seu IMC e {}.  \033[1;33mProcure um medico voce esta obeso.\033[m".format(imc))
else:
    print("Seu IMC e {}. \033[1;91mProcure um medico com urgencia voce esta com obesidade morbida, corre risco de vida.\033[m".format(imc))
