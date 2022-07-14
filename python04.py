


import time 


try:
    a = int(input("Escolha 1 ou 2 :)\n--> "))
    if a == 1:
        b = [ i for i in range(8E8) ] 
        for i in b:
            print(b)
            break
    elif a == 2:
        c = ( i for i in range(8E8) )
        for i in c:
            print(c)
            break
    else:
        pass
except: 
    print(":((((((((((((")