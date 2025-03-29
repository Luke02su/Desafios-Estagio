def val2Maior(val1, val2):
    
    cont = int
    
    if val2 > val1:
        while val2 >= val1: 
            cont += val1
            val1 += 1
    else:
        val2 = int(input('Digite um valor maior que o primeiro valor: '))
        val2Maior(val1, val2) 
        return

    print('Soma dos intervalos:', cont)

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

val2Maior(val1, val2)
