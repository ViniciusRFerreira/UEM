def func_matriz(matriz):
    '''
    Recebendo os valores da M[4][3] e mostrando a soma deles
    Exemplos:
    >>> func_matriz([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    78
    >>> func_matriz([[2,5,7],[9,11,13],[15,17,19],[21,23,25]])
    167
    '''
    soma = 0
    for i in range(0,4):
        for j in range(0,3):
            soma += matriz[i][j]
    return soma
   

def entrada():
    matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,4):
        for j in range(0,3):
            num = float(input('Informe um número: \n'))
            matriz[i][j] = num
    soma = func_matriz(matriz)
    print(f'\n - Soma: {soma}')
    

entrada()