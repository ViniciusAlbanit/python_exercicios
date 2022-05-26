from time import sleep

def relogio():
    while True:
        h=0
        while h < 24:
            m=0
            while m < 60:
                s=0
                while s < 60:
                    print(f'{h:02}:{m:02}:{s:02}')
                    s +=1
                    sleep(1)
                m +=1
            h +=1
