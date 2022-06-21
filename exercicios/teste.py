n = int(input("Que termo deseja encontrar: "))
ult=1
penul=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ult + penul
        penul = ult
        ult = termo
        count += 1
print(termo)
    
