a = int(input('Faturamento do dia 1: '))
cont = 1
soma = a
meses = []
maiores = []
meses.append(a)
while cont < 30:
    cont += 1
    b = int(input(f'Faturamento do dia {cont}: '))
    meses.append(b)
    soma += b
    meses.sort()
media = soma / cont
for i in meses:
    if i >= media:
        maiores.append(i)
print(f'Os valores que passaram a média no mês: {maiores}')
print(f'Esse é o menor valor do mês: {meses[0]}')
print(f'Esse é o maior valor do mês: {meses[29]}')
