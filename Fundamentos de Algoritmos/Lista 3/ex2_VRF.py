'''
- Algoritimo para verificar se uma lista de números está em ordem decrescente
'''
def decresc(lista):
    '''
    Exemplos:
    >>> decresc([5,4,3,2,1])
    True
    >>> decresc([5,4,2,7,9])
    False
    '''
    for i in range(len(lista)):
        if i > 0:                    
            if lista[i] > lista[i-1]:
                return False
    return True


def entrada():
    lista = [9,8,7,6,5,4,3,2]
    saida = decresc(lista)

    if saida == True:
        print('\n - A lista está em ordem decrescente.\n')
    elif saida == False:
        print('\n - A lista não está em ordem decrescente.\n')

entrada()
