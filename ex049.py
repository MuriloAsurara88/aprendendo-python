
while True:
        num = int(input("Escreva o numero que deseja a tabuada: "))
        for n in range(1, 11):
                print(12 * '=')
                print('{}  x {:2} = {}'.format(num, n, num * n))
                if num <= 0:
                        break
        print("Progama encerrado. Volte Sempre!")
        print("-=-"*15)
