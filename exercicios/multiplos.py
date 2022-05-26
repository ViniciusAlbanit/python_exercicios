a, b=input().split()
a=int(a)
b=int(b)
if a%b==0 or b%a==0:
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')
