a=int(input())
qtd=0
soma=0
while a > 0:
    qtd +=1
    soma +=a
    media = soma/qtd
    a=int(input())
print(f'{media:.2f}')

