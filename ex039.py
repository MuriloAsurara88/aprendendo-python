from datetime import date
nasc = int(input("Informe o ano de nascimento: "))
atual = date.today().year
idade = atual - nasc
sexo = str(input("Qual o seu sexo (f/m): "))
print("Quem nasceu em {} tem {} anos.".format(nasc, idade))
if sexo == ("f"):
    print("Mulheres nao sao obrigadas a se alistarem no servico militar.")
else:
    if idade == 18:
        print("Voce deve se alistar imediatamento.")
    elif idade < 18:
        falta = 18 - idade
        print("Voce ainda nao tem idade para se alistar, faltam {} anos.".format(falta))
    else:
        falta = idade - 18
        print("Seu prazo de alistamento ja passou em {} anos, procure uma junta militar com urgencia.".format(falta))
