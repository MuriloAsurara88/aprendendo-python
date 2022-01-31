""" Importado a biblioteca math inteira
import math
ang = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(ang))
print("Para o Ângulo {} o seno é {:.2f}".format(ang, sen))
cos = math.cos(math.radians(ang))
print("Para o Ângulo de {}, o cosseno é {:.2f}".format(ang, cos))
tang = math.tan(math.radians(ang))
print("Para o Ângulo de {}, a tangente é {:.2f}".format(ang, tang))"""


"""Importado da biblioteca apenas as expressões radians, sin, cos, tan"""
from math import radians, sin, cos, tan
ang = float(input("Digite o valor do ângulo: "))
sen = sin(radians(ang))
print("Para o ângulo {}, o valor de seno é: {:.2f}".format(ang, sen))
cos = cos(radians(ang))
print("Para o ângulo {}, o valor de cosseno é: {:.2f}".format(ang, cos))
tang = tan(radians(ang))
print("Para o ângulo {}, o valor da tangente é: {:.2f}".format(ang, tang))
