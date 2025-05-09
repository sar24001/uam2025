'''
Autor: Maria A. Sarante. S
Fecha: 
Version:
Descripcion:
'''
def contarPares():
    lim= int(input("Digite el numero limite: "))
    cont= 0 #Incializacion de controles de variables
    while(cont<= lim): #control del bucle
        if(cont % 2 == 0):
            print(f"{cont} es un numero par")
        cont+=1 #actualizacion de la variable de control
    print("------------------------------------")
    print(f"{cont} es igual o menor que {lim}")