#Vinícius Ramon Ferreira
def entrada():
    '''Código para receber x,y e z e verificar se é possivel formar um triângulo com os mesmos, e depois verificar qual o tipo de triângulo formado.
    Exemplos:
    >>> valido(5,4,3)
    True
    >>> valido(2,3,6)
    False
    >>> tipo_triangulo(5,5,5)
    'Triângulo Equilátero'
    >>> tipo_triangulo(5,4,4)
    'Triângulo Isóceles'
    >>> tipo_triangulo(5,4,3)
    'Triângulo Escaleno'
    '''

    x = float(input('X: '))
    y = float(input('Y: '))
    z = float(input('Z: '))
    saida = valido(x,y,z)
    if saida == True:
        saida = tipo_triangulo(x,y,z)
        print(saida)
    elif saida == False:
        print('\nTriângulo Inválido!')

def valido(x,y,z):
    if x > 0 and y > 0 and z > 0:
        if (x < (y + z)) and (y < (x + z)) and (z < (x +y)):
            return True
        else:
            return False
    else:
        return False
                       
def tipo_triangulo(x,y,z):
    if x == y == z:
        return 'Triângulo Equilátero'
    elif x == y or x == z or y == z:
        return('Triângulo Isóceles')
    else:
        return('Triângulo Escaleno')

entrada()