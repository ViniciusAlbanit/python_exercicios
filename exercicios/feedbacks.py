qtd_dias= int(input())
for i in range(qtd_dias):
    qtd_feedbacks = int(input())
    for j in range(qtd_feedbacks):
        feedback =int(input())
        if feedback ==1:
            print('Rolien')
        elif feedback ==2:
            print('Neaj')
        elif feedback==3:
            print('Elehcim')
        else:
            print('Odranel')
