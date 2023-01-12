lista =  [20,15,12,11,8,4,1]
menor = lista[0]
for i in range(len(lista)-1):
    if menor > lista[i+1]:
        menor = lista[i+1]

lista.remove(menor)
suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]
promedio = suma /len(lista)
print(promedio)





