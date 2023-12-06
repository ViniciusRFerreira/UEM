#Vinícius Ramon Ferreira
def entrada():
    ''' Códiigo para calcular o valor total da compra de laranjas, variando o preço de acordo com a quantidade comprada.
    Exemplos:
    >>> valor_laranjas(10)
    'R$3.5'
    >>> valor_laranjas(16)
    'R$4.8'
    '''


    quantidade = float(input('Quantidade de laranjas compradas: '))
    saida = valor_laranjas(quantidade)
    if saida != False:
        print(saida)
    elif saida == False:
        print('\n - Informe um valor válido de laranjas!')

def valor_laranjas(quantidade):
    if quantidade < 1:
        return False
    else:
        if quantidade < 12:
            valor = quantidade * 0.35
        elif quantidade >= 12:
            valor = quantidade * 0.30
    
        return(f'R${valor}')

entrada()