"""Usando biblioteca math"""

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))

""" tambem pode ser feito conforme abaixo
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, int(num)))"""

