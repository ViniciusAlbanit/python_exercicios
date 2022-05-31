divida=int(input())
valor=int(input())
pagamento = divida - valor
qtd=1
if divida < valor:
    print(f'pagamento: {qtd}')
    print(f'antes = {divida}')
    print(f'depois = 0')
    print(f'-----')
else:   
    while pagamento >= 0:
        print(f'pagamento: {qtd}')
        print(f'antes = {divida}')
        print(f'depois = {pagamento}')
        print(f'-----')
        divida = pagamento
        pagamento -= valor 
        qtd +=1
        if pagamento < 0:
            print(f'pagamento: {qtd}')
            print(f'antes = {divida}')
            print(f'depois = 0')
            print(f'-----')
        
