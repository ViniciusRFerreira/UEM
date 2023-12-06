def principal():
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            num = float(input('Informe um número: \n'))
            matriz[i][j] = num
    maior(matriz)

def maior(matriz):
    '''
    Calculando maior elemento da diagonal principal e dividindo os valores da matriz por ele e colocando-os em outra matriz
    Exemplos:
    >>> maior([[1,2,3],[4,5,6],[7,8,9]])
    [[0.11, 0.22, 0.33], [0.44, 0.56, 0.67], [0.78, 0.89, 1.0]]
    >>> maior([[2,4,6],[8,10,12],[14,16,18]])
    [[0.11, 0.22, 0.33], [0.44, 0.56, 0.67], [0.78, 0.89, 1.0]]
    '''
    maior = 0
    for i in range(0,3):
        for j in range(0,3):
            if i == j:
                if maior < matriz[i][j]:
                    maior = matriz[i][j]
    matriz2(matriz,maior)

def matriz2(matriz,maior):
    matriz2 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            matriz2[i][j] = round(matriz[i][j] / maior,2)
    print(f'{matriz2}')

principal()