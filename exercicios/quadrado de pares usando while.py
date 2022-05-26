a=int(input())
qtd=0
while qtd != a:
    qtd +=1
    if qtd%2==0:
        quadrado=(qtd**2)
        print(f'{qtd}^2 = {quadrado}')
