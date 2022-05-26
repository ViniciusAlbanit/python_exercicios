maior_valor=int(input())
posicao_maior=1
posicao=2
while posicao <= 6:
    x=int(input())
    if x>maior_valor:
        maior_valor=x
        posicao_maior = posicao
    posicao +=1
print(maior_valor)
print(posicao_maior)
