def fatorial(n):
    #Função retirada do exercício anterior
    if n == 0:
        return 1
    else:
        return fatorial(n-1)*n

def serie(n):
    ''' 
    Função para calcular a série S
    Exemplos:
    >>> serie(4)
    2.708333333333333
    >>> serie(10)
    2.7182818011463845
    '''
    if n == 0:
        return 1
    else:
        return (1/fatorial(n)) + serie(n-1)

def entrada():
    n = int(input('N: '))
    saida = serie(n)
    print(round(saida,2))

#entrada()