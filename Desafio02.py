temperatura = [23.6, 37.9, 25.1, 19.0, 29.8];

minTemp = min(temperatura)
maxTemp = max(temperatura)
somaTemp = sum(temperatura)
contTemp = len(temperatura)
mediaTemp = float(somaTemp / contTemp)

print('Temperatura mínima:', minTemp)
print('Temperatura máxima:', maxTemp)
print('Temperatura média:', round(mediaTemp, 1))
