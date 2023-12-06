def verifica_4(lista):
    x = False
    i = 0
    while i < 4 and i < len(lista):
        if lista[i] != []:
            print(f'\n{i}\n')
            i += 1
        else:
            return True
    return x

def entrada():
    lista = []
    val = 0
    while val != -1:
        val = float(input('Digite valores: '))
        if val != -1:
            lista.append(val)
    saida = verifica_4(lista)
    print(saida)

entrada()