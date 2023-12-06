def esta(lista,ver):
    i = 0
    x = False
    while x == False and i < len(lista):
        if ver == lista[i]:
            x = True
        else:
            x = False
        i += 1
    return x


def entrada():
    lista = [1,2,3,4,5,6,7,8,9]
    ver = int(input('Número na lista? '))
    saida = esta(lista,ver)
    print(saida)

entrada()