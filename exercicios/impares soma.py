def impar(n):
    return n%2==1
x=int(input())
y=int(input())
soma=0
i=x + 1
while i < y:
    if impar(i):
        soma +=i
    i +=1
print(soma)    
