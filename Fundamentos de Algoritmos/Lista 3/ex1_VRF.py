'''
- Algoritimo para receber uma lista de valores e retornar o maior deles e a casa em que o mesmo é encontrado
'''
def maior(lista):
    '''
    Exemplos:
    >>> maior([10,11,12,13,9])
    (13, 3)
    >>> maior([25,43,97,65])
    (97, 2)
    '''
    maior = 0
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
            indice = i
    return maior,indice

def entrada():
    lista = [1,2,3,4,32,2342,89,1234]
    maior_num,indice = maior(lista)
    print(f'O maior número é {maior_num} e foi localizado pela primeira vez na {indice}ª posição da lista.')

entrada()