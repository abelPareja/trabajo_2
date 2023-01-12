lista= []
tamaño = int(input("ingrese el tamaño dela lista"))
numero = int(input("ingrese un numero"))
for i in range(1,tamaño+1):
    lista.append(numero*i)
for i in lista:
    print(i)