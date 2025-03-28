import random
import array

lista = array.array('i')

for i in range(0, 50):
    numerosAleatorios = random.randint(0, 100)
    lista.append(numerosAleatorios)
print(lista)


    
