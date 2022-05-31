a=int(input())
b=int(input())
qtd=0
d=1
for i in range(a, b+1):
    while d <= i:
        if i%d==0:
            qtd +=1
        d +=1
        if qtd%2 == 0:
            print(i)

print(f'primos {qtd}')
    
