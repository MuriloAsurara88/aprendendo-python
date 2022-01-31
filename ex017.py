""" formula matematica
co = float(input("Qual é o valor do cateto oposto: "))
ca = float(input("Qual é o valor do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("o valor da hipotenusa é: {:.2f}".format(hi))"""

""" importando a biblioteca math inteira
import math
co = float(input("Qual é o valor do cateto oposto: "))
ca = float(input("Qual é o valor do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa mede: {:.2f}".format(hi)"""

"""Importando a função hypot da biblioteca math"""
from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hi = hypot(ca, co)
print("A hipotenusa mede: {:.2f}".format(hi))
