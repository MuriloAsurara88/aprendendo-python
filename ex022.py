nome = str(input("Digite o seu nome inteiro: ")).strip()
print("Seu nome em letras maiúsculas: {}".format(nome.upper()))
print("Seu nome em letras minúsculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")))
print("Seu Primeiro nome tem {} letras".format(nome.find(" ")))

"""
Pode usar a expressão abaixo para o mesmo resultado.
separa = nome.split()
print("Seu primeiro nome é {} e tem {} letras.".format(separa[0], len(separa[0])))
"""





