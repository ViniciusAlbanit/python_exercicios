Alunos = {}

for _ in range(2):
    ra = int(input('RA? '))
    nota1 = float(input('Nota1? '))
    nota2 = float(input('Nota2? '))
    nota3 = float(input('Nota3? '))
    Alunos[ra] = nota1, nota2, nota3
    print()
    
print('-' * 30)
for nota1, nota2, nota3 in Alunos.values():
    media = (nota1 + nota2 + nota3) / 3
    print(media)
