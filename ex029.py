vel = float(input("Qual a Velocidade do veículo em Km/h: "))
multa = 7 * (vel-80)
if vel > 80:
    print("Velocidade acima do permitido, você será multado em {:.2f} R$.".format(multa))
else:
    print("Obrigado por dirigir em segurança, sua Vida não tem preço!")
