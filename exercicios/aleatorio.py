from random import randint

def aleatorio(qtd):
    L = []
    for i in range(qtd):
        L.append(randint(10,90))
    return L
