def divisivel(x,y):
    return x%y==0
n = int(input())
for _ in range(n):
    x = int(input())
    soma= 0
    for divisor in range(1,x):
        if divisivel(x,divisor):
            soma += divisor
    if soma == x:
       print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
    
