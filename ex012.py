n = float(input('Digite o valor do produto sem desconto: '))
proddesc = n - (n * 0.05)
print('O valor do produto é {} R$. Com o desconto sai por {} R$.'.format(n, proddesc))
