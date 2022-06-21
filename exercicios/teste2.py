sp= 67836430
rj= 3667866
mg= 2922988
es= 2716548
outros= 1984953
escolha =int(input('Qual estado quer calcular: 1 sp, 2 rj, 3 mg, 4 es, 5 outros '))
porce=float(input())
if escolha == 1:
    resul= sp * porce/100
    print(resul)
elif escolha == 2:
    result= rj * porce/100
    print(resul)
elif escolha == 3:
    resul= mg * porce/100
    print(resul)
elif escolha == 4:
    resul= es * porce/100
    print(resul)
else:
    resul= outros * porce/100
    print(resul)
