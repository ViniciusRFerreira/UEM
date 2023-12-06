#Escreva uma funcao que receba um numero inteiro N e retorne uma lista com os N primeiros numeros primos.

def primeiros_primos(n):
    '''
    Recebendo um valor N e escrevendos os N's primeiros valores primos.
    Exemplos:
    >>> primeiros_primos(23)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
    >>> primeiros_primos(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
    '''
    lista = []

    while len(lista) < n:
        if n > 0:
            for i in range(1,100000):
                x = 0
                for j in range(1,100000):
                    if i % j == 0:
                        x += 1
                if x < 3 and i != 1:
                    lista.append(i)
                    if len(lista) == n:
                        return lista

def entrada():
    n = int(input('N: '))
    saida = primeiros_primos(n)
    print(saida)

entrada()