credito=float(input('Credito? R$'))
while credito > 0:
    item = float(input('Item? R$'))
    if item > credito:
        print('Negado! Ultrapassa seu credito!')
        break
    credito -= item
print(f'Credito restante: {credito:.2f}')
