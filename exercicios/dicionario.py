D = {}
for _ in range(5):
    nome = input('Nome? ')
    preco = float(input('Preço? '))
    D[nome] = preco
    print()

print('-' * 30)

for item in D.items():
    if item[1] > 50.0:
        print('Produto: ', item[0])
    
