def fatorial(n):
    ''' 
    Função para calcular o fatorial de um valor N
    Exemplos:
    >>> fatorial(5)
    120
    >>> fatorial(10)
    3628800
    '''
    if n == 0:
        return 1
    else:
        return fatorial(n-1)*n

def entrada():
    n = int(input('N: '))
    saida = fatorial(n)
    print(saida)

#entrada()