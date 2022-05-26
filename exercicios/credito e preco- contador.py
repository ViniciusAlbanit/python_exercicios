credito=float(input('Credito? '))
total=0
posicao=1
preco=float(input(f'Preço do item {posicao}? '))
while credito >= preco:
    total += preco
    credito -= preco
    posicao +=1
    preco=float(input(f'Preço do item {posicao}? '))
print(f'Total da compra: R$ {total:.2f}')
print(f'Credito restante: R$ {credito:.2f}')
