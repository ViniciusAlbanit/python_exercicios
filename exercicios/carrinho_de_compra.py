item=input()

carrinho=[]

while item !='':
    inteiro=int(item)
    carrinho.append(item)
    item=input()
    
comando, item_novo=input().split()
item_novo=int(item_novo)
if comando == 'adicionar':
    carrinho.append(item_novo)
elif comando == 'remover':
    carrinho.remove(item_novo)
elif comando == 'exibir' and item_novo == '':
    print(carrinho)





