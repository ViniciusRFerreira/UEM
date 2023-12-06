def quantidade_vezes(arranjo, num, n):
    '''
    >>> quantidade_vezes([4, 1, 3, 4, 3, 2, 4, 4], 4, 8)
    4
    >>> quantidade_vezes([2, 8, 6, 4, 1, 9], 2, 6)
    1
    '''
    if n == 0:
        return 0
    if arranjo[n-1] == num:
        return 1 + quantidade_vezes(arranjo, num, n-1)
    else:
        return quantidade_vezes(arranjo, num, n-1)