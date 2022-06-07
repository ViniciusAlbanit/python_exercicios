def cria_matriz(L, C):
    M = []
    linha = C * [0]
    for i in range(L):
        M.append(linha[:])
    return M
def preenche_matriz(M, L, C):
    for i in range(L):
        for j in range(C):
            M[i][j] = float(input())
M = cria_matriz(12,12)
L = int(input())
T = input()
preenche_matriz(M, 12, 12)
if T == 'S':
    resultado = sum(M[L])
else:
    resultado = sum(M[L]) / 12
print(f'{resultado:.f}')
