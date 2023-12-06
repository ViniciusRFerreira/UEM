def naodecresc(arranjo, n):
    '''
    >>> naodecresc([1, 2, 5, 6], 4)
    'Não Decrescente'
    >>> naodecresc([4, 2, 1], 3)
    'Decrescente'
    '''
    if n == 1: 
        return 'Não Decrescente'
    if n == 2 and arranjo[0] > arranjo[1]:
        return 'Decrescente'
    if arranjo[n-2] > arranjo[n-1]:
        return 'Decrescente'
    return naodecresc(arranjo, n-1)