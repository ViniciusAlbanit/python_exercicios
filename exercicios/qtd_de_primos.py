a=int(input())
b=int(input())
qtd=0
for i in range(a, b+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            qtd +=1
            print(f'{i}')
print(f'Primos: {qtd}')
            
    
