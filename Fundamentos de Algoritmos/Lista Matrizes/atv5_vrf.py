def caca_palavra():
    '''
    Fazer uma espécie de caça palavras usando matrizes.
    Exemplos:
    >>> caca_palavra()
    [0, 4, 0, 7, 1, 1, 4, 1]
    '''
    M =[['A','C','A','S','A','M','O','R','S','W','B'],
        ['C','A','X','R','F','T','P','A','S','A','C'],
        ['A','M','X','A','O','J','R','W','T','F','A'],
        ['S','O','E','O','W','M','Q','Z','O','G','B'],
        ['A','R','Y','K','F','W','C','A','A','R','B']]

    s = 'AMOR'
    lista = []
    for l in range(0,2):
        for c in range(0,9):
            if M[l][c] == s[0] and M[l][c+1] == s[1] and M[l][c+2] == s[2] and M[l][c+3] == s[3]:
                lista.append(l)
                lista.append(c)
                lista.append(l)
                lista.append(c+3)
            if M[l][c] == s[0] and M[l+1][c] == s[1] and M[l+2][c] == s[2] and M[l+3][c] == s[3]:
                lista.append(l)
                lista.append(c)
                lista.append(l+3)
                lista.append(c)

    return lista

lista = caca_palavra()
for i in range(0,len(lista),4):
    print(f'\n - Da linha {lista[i]} e coluna {lista[i+1]}.')
    print(f'Até a linha {lista[i+2]} e coluna {lista[i+3]}.\n')