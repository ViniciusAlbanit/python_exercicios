a=float(input())
if a>=0 and a<=25:
    print(f'Intervalo [0,25]')
elif a>25 and a<=50:
    print(f'Intervalo (25,50]')
elif a>50 and a<=75:
    print(f'Intervalo (50,75]')
elif a>75 and a<=100:
    print(f'Intervalo (75,100]')
else:
    print(f'Fora do intervalo')
