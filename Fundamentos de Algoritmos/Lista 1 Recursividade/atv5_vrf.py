def mult(x,y):
    '''
    Função para calcular a multiplicação de um número X por um número Y, através de somas sucessivas
    Exemplos:
    >>> mult(4,10)
    40
    >>> mult(5,6)
    30
    '''
    if x == 0:
        return 0
    else:
        return mult(x-1,y)+y

def entrada():
    lista = []
    x = int(input('1° Número: '))
    y = int(input('2° Número: '))
    saida = mult(x,y)
    ystr = str(y)

    for i in range(x):
        lista.append(ystr)
        if i != x-1:
            lista.append('+')

    print(', '.join(lista))
    print(f'{saida}')

#entrada()