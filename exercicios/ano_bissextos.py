a=int(input())
b=int(input())
qtd=0

for i in range(a, b+1):
    if (i%4 == 0 and i%100 != 0) or i%400 == 0:
        qtd +=1
        print(i)
            
print(f'bissextos: {qtd}')
    
