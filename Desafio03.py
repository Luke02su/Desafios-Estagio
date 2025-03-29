import random
import array

array = array.array('i')

for i in range(50):
    numerosAleatorios = random.randint(0, 100)
    array.append(numerosAleatorios)

lista = list(array)

posicoes = {}

for idx, num in enumerate(lista):
    if num in posicoes:
        posicoes[num].append(idx)
    else:
        posicoes[num] = [idx]

repetidos = {num: pos for num, pos in posicoes.items() if len(pos) > 1}

if repetidos:
    print('Números repetidos e suas posições:')
    for num, pos in repetidos.items():
        print('Número', num, 'aparece nas posições', pos)
else:
    print('Não há números repetidos.')

print('\nLista de números gerados:')
print(lista)
