D = {}
for _ in range(5):
    nome = input('Nome? ')
    preco = float(input('Preço? '))
    D[nome] = preco
    print()

print('-' * 30)

for nome, preco in D.items():
    if preco > 50.0:
        print('Produto: ', nome)
    
