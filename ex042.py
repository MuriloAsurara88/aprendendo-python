r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triangulo ", end="")
    if r1 == r2 == r3:
        print("EQUILATERO.")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO.")
    else:
        print("ISOSCELES.")
else:
    print("Os seguimentos acima NAO PODEM formar um triangulo.")