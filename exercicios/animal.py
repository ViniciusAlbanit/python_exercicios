a=input()
b=input()
c=input()
if a=='vertebrado' and b=='ave' and c=='carnivoro':
    animal= 'aguia'
if a=='vertebrado' and b=='ave' and c=='onivoro':
    animal= 'pomba'
if a=='vertebrado' and b=='mamifero' and c=='onivoro':
    animal= 'homem'
if a=='vertebrado' and b=='mamifero' and c=='herbivoro':
    animal= 'vaca'
if a=='invertebrado' and b=='inseto' and c=='hematofago':
    animal= 'pulga'
if a=='invertebrado' and b=='inseto' and c=='herbivoro':
    animal= 'lagarta'
if a=='invertebrado' and b=='anelideo' and c=='hematofago':
    animal= 'sanguessuga'
if a=='invertebrado' and b=='anelideo' and c=='onivoro':
    animal= 'minhoca'

print(animal)
