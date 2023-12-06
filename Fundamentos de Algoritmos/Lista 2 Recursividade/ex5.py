def valormáximo(arranjo, n):
    '''
    >>> valormáximo([2, 9, 14, 3], 4)
    14
    >>> valormáximo([2, 4, 10, 35], 4)
    35
    '''
    if n == 1:
        return arranjo[0]

    m = valormáximo(arranjo, n-1)
  
    if m > arranjo[n-1]:
        return m
    else:
        return arranjo[n-1]