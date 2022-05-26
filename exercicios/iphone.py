def  divisao(x,y):
    qtd=0

    while x >= y:
        x -=y
        qtd +=1
    return qtd
x=int(input())
y=int(input())

print(f'Resposta = {divisao(x,y)}')
