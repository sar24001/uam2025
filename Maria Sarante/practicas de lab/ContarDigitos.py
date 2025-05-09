'''
Autor: Maria A. Sarante. S
Fecha: 
Version:
Descripcion:
'''
import os

def contarDigitos():
    os.system("cls")
    cont= 0
    num = int(input("Digite un numero entero positivo de n digitos: "))
    div= num
    while(div != 0):
        mod=div % 10
        print(f"{mod} es un digito del numero {num}")
        div= int(div/10) #actualizacion de la variable de control
        cont+=1
    print(f"La cantidad de digitos de {num} es {cont}")