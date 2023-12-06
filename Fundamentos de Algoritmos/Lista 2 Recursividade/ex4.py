def arr_binario(arranjo, n):
    '''
    >>> arr_binario([0, 1, 2, 1, 3, 1], 6)
    'Não Binário'
    >>> arr_binario([0, 1, 0, 1, 0, 0], 6)
    'Binário'
    '''
    if n == 0:
        return 'Binário'
    
    if arranjo[n-1] != 0 and arranjo[n-1] != 1:
        return 'Não Binário'
    
    return arr_binario(arranjo, n-1)