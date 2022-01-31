while True:
        print(15 * '=')
        num = int(input("Escreva o numero que deseja a tabuada: "))
        print(15 * '=')
        if num < 0:
                break
        for n in range(1, 11):
                print(f'{num}  x {n:2} = {num * n}')
print("Progama encerrado. Volte Sempre!")
print("-=-"*15)