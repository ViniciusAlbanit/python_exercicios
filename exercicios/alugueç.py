divida=int(input())
valor=int(input())
pagamento = divida - valor
qtd=1
while pagamento >= 0:
    print(f'pagamento: {qtd}')
    print(f'antes = {divida}')
    print(f'depois = {pagamento}')
    print(f'----')
    divida = pagamento
    pagamento -= valor 
    qtd +=1
