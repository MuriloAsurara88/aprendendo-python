dias = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantos Km você rodou com o carro: '))
td = dias * 60
tk = km * 0.15
total = td + tk
print('Você ira pagar {:.2f} pelo aluguel do veiculo.'.format(total))
