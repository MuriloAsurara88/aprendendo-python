n = float(input('Quanto dinheiro você tem em R$: '))
dol = n / 5.64
eur = n / 6.38
print('Você pode comprar com {:.2f} R$, {:.2f} US$ ou {:.2f} Euros .'.format(n, dol, eur))
