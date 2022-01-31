print("-==-"*20)
print("Analisador de Triangulos")
print("-==-"*20)
r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar um triangulo!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")
