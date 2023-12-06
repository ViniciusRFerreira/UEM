#Escreva uma fun ̧c ̃ao que receba um n ́umero inteiro N e retorne uma lista com os numeros primos at ́e N;
matriz = []  
def entrada():
    '''
    Recebendo um número N inteiro e retornando os números primos até N
    Exemplos:
    >>> primos_n(7)
    [2, 3, 5, 7]
    >>> primos_n(23)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    '''
    n = int(input('N: '))
    saida = primos_n(n)
    print(saida)

def primos_n(n):
    x = 0
    lista = []
    if n > 0:
        for i in range(1,n+1):
            x = 0
            for j in range(1,n+1):
                if i % j == 0:
                    x += 1
            if x < 3 and i != 1:
                lista.append(i)
    return lista

entrada()