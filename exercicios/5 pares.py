def par(n):
    return n%2==0
n=int(input())
qtd=0
x=0

while qtd < n:
    if par(x):
        print(x)
        qtd +=1
    x +=1
print('Fim') 
