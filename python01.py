import time 
import os 

def cc():
    os.system("clear")
# Temporizador 
while True:
    os.system("clear")
    print("-- Temporizador -- ")
    try:
        option = int(input("Digite o tempo em segundos\n--> "))
        i = 0
        for i in range(option):
            cc()
            i+=1
            print(f"{i} Segundos")
            time.sleep(1)
        print(f"Se passaram {i} segundos!")
        break
    except:
        cc()
        print("Digite um valor numérico!")
        time.sleep(2)
        cc()
