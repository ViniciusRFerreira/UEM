def elevado(a,n):
    '''
    Função para elevar um valor A por um valor N
    Exemplos:
    >>> elevado(2,4)
    16
    >>> elevado(3,3)
    27
    '''
    if n == 0:
        return 1
    else:
        return a*elevado(a,n-1)

def entrada():
    a = int(input('A: '))
    if a == 0:
        print('Erro')
    
    n = int(input('N: '))
    if n < 0:
        print('Erro')
    
    saida = elevado(a,n)
    print(saida)

#entrada()