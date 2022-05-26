n= int(input())
contador=0
while contador < n:
    x=int(input())

    qtd=0
    d=1
    while d <= x:
        if x%d==0:
            qtd +=1
        d +=1
    if qtd==2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
    contador +=1
