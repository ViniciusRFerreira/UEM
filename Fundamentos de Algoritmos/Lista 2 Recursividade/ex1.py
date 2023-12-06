def soma(arranjo,n):
    '''
    Somar elementos de um arranjo.
    >>> soma([1, 2, 3, 5], 4)
    11
    >>> soma([2, 2], 2) 
    4
    '''
    if n == 0:
        return 0
    
    return arranjo[n-1] + soma(arranjo, n-1)