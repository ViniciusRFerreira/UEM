def pares(arranjo, n):
    '''
    >>> pares([1, 4, 6, 9], 4)
    'Não todos pares'
    >>> pares([2, 4, 16, 22], 4)
    'Pares'
    '''
    if n == 0:
        return 'Pares'

    if arranjo[n-1] % 2 != 0:
        return 'Não todos pares'
  
    return pares(arranjo, n-1)