def calcular_notas(lista_notas):
    notas_finais = []
    for nota in lista_notas:
        if nota < 38:
            notas_finais.append(nota)
        else:
            proximo_multiplo = nota + (5 - nota % 5)
            if proximo_multiplo - nota < 3:
                notas_finais.append(proximo_multiplo)
            else:
                notas_finais.append(nota)
    return notas_finais

notas = [73, 67, 38, 33]

notas_finalizadas = calcular_notas(notas)
print("Notas finais:", notas_finalizadas)
