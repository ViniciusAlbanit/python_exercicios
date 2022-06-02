a=int(input())
pontuacao_joao = 0
pontuacao_maria = 0
for i in range(a):
    for j in range(0, 3):
            x, d = input().split()
            x = int(x)
            d = int(d)
            pontuacao1 = x * d
            pontuacao_joao += pontuacao1
    for k in range(0, 3):
            x, d = input().split()
            x = int(x)
            d = int(d)
            pontuacao2 = x * d
            pontuacao_maria += pontuacao2
    if pontuacao_joao > pontuacao_maria:
            print(f'JOAO')
            pontuacao_joao -=pontuacao_joao
            pontuacao_maria -=pontuacao_maria
            
    else:
            print(f'MARIA')
            pontuacao_maria -=pontuacao_maria
            pontuacao_joao -=pontuacao_joao
        
    
