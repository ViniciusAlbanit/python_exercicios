def misterio():
    x= 200
    def enigma():
        y= x + 300
        return y
    return 2*x + enigma()
x = 1000
z= misterio()
print(f'z = {z}')
