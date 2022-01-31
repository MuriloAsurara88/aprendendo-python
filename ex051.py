print("="*10)
print(">>>>>10 primeiros termos de um PA <<<<<")
print("="*10)
i = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
dec = i + (10-1) * r
for n in range(i, dec + r, r):
    print(n)
print("FIM")
