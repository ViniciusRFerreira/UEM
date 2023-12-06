def soma(n):
    '''
    Funcão para calcular a soma dos valores, até um valor N
    Exemplos:
    >>> soma(4)
    10
    >>> soma(10)
    55
    '''
    if n == 0:
        return 0
    else:
        return soma(n-1)+n

def entrada():
    n = int(input('N: '))
    saida = soma(n)
    print(saida)

#entrada()