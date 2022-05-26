def par(n):
    return n%2==0

def tabuleiro(n):
    linha=0
    while linha < n:
        coluna = 0
        while coluna < n:
            if par(linha+coluna):
                print(2*chr(9608), end='')
            else:
                print(2 * ' ' , end='')
            coluna += 1
        print()
        linha +=1

