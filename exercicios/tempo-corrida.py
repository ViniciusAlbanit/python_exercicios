tempo = int(input())
soma=0
qtd=0
lista=[]

while tempo > -1:
    lista.append(tempo)
    soma +=tempo
    qtd +=1
    tempo=int(input())

media = soma / qtd


print(f'MEDIA: {media:.2f}')
for i in lista:
    if i < media:
        print(i)
