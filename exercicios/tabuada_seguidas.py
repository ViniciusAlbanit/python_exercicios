primeira_tabuada=int(input())
segunda_tabuada=int(input())

if segunda_tabuada < primeira_tabuada:
    print(f'Nenhuma tabuada no intervalo!')
else:
    for i in range(primeira_tabuada, segunda_tabuada +1):
        for j in range(1,11):
            print(f'{i} x {j} = {i * j}')
        print('-'*10)
