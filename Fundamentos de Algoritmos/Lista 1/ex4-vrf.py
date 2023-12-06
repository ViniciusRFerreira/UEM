#Vinícius Ramon Ferreira
def entrada():
    '''Código para receber a média final de um determinado aluno e verificar seu conceito A, B, C, D.
    Exeplos:
    >>> conceito(2.0)
    'Conceito D'
    >>> conceito(6.0)
    'Conceito C'
    >>> conceito(8.0)
    'Conceito B'
    >>> conceito(10.0)
    'Conceito A'
    '''
    

    media_aluno = float(input('Média Final do aluno: '))
    saida = conceito(media_aluno)
    if saida != False:
        print(saida)
    elif saida == False:
        print('Valor de média inválido!')

def conceito(media_aluno):
    
    if media_aluno < 0:
        return False
    elif media_aluno >= 0 and media_aluno <= 4.9:
        return ('Conceito D')
    elif media_aluno <= 6.9:
        return ('Conceito C')
    elif media_aluno <= 8.9:
        return ('Conceito B')
    elif media_aluno <= 10.0:
        return ('Conceito A')
    elif media_aluno > 10.0:
        return False
    

entrada()