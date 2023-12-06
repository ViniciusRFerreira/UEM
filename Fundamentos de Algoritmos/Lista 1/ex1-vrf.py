#Vinícius Ramon Ferreira
def verifica(senha):
    '''Função para verifica se a senha digitada está correta para liberar o acesso.
    Exemplos:
    >>> verifica('asdasdad')
    False
    >>> verifica('Giva123')
    True
    '''

    if senha == 'Giva123':
        return True
    else:
        return False

def entrada():
    senha = input('Insira a senha: ')
    saida = verifica(senha)
    
    if saida == True:
        print('\nSenha Correta - Acesso Liberado')
    else:
        print('\nSenha Incorreta - Acesso Negado')

entrada()