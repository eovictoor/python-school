import os 
import time
def cc():
    os.system("clear")

#percorrendo Lista por Caracteres chaves

search = str(input("Digite 2 caracteres para realizar a busca\n--> "))



lista = ["bola", "machado", "banana", "marreta", "faca", "foice", "moto", "motocicleta", "carro", "carroca"]

if len(search) == 1:
    for item in lista:
        if item[0] == search[0]:
            print(item)
elif len(search) == 2:
    for item in lista:
        if item[0]+item[1] == search[0]+search[1]:
            print(item)
else:
    print("Opa :(")
