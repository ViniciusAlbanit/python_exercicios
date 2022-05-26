def par(n):
    return n%2==1
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
qtd = 0
if par(a): qtd +=1
if par(b): qtd +=1
if par(c): qtd +=1
if par(d): qtd +=1
if par(e): qtd +=1

print(f'{qtd} valores pares')
