n=int(input())
soma=1
while n >= 1:
    fat=n*soma
    soma=fat
    n -=1
print(f'{fat}')

