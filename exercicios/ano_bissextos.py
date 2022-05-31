a=int(input())
b=int(input())
qtd=0

for i in range(a, b+1):
    if i%4 == 0 or i%400 == 0:
        print(i)
        qtd +=1
            
print(f'bissextos: {qtd}')
    
