def converte_inteiro(lista):

   for i in range(len(lista)):

       lista[i] = int(lista[i])

def exibe(carrinho):

   for i in range(len(carrinho)):

       if i < len(carrinho) -1:

           print(carrinho[i], end=' ')

       else:

           print(carrinho[i])

carrinho = input().split()

if carrinho != []:

   converte_inteiro(carrinho)

comando = input().split()

while comando[0] != 'encerrar':

   if comando[0] == 'adicionar':

       carrinho.append(int(comando[1]))

   elif comando [0] == 'remover':

       comando[1] = int(comando[1])

       if comando [1] in carrinho:

            carrinho.remove(comando[1])

       else:

            print(f'código {comando[1]} não encontrado')

   else:

       carrinho.sort()        

       exibe(carrinho)  

   comando = input().split()  

carrinho.sort()        

exibe(carrinho)
