import time 
import os
def cc(): os.system("clear") 
cc()
try:
    i = 0 
    numero = int(input("\nCalculadora\nDigite um numero --> "))
    for i in range(0,10):
        i+=1
        print(f"{i} x {numero} = {i*numero}")
except:
    cc()
    print("Digite um valor numérico!")
    time.sleep(1)
    cc()
