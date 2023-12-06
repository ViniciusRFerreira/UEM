#Vinícius Ramon Ferreira
def idade_media(idade1,idade2,idade3,idade4):
    '''Função para receber o valor da idade de 4 pessoas, encontrar a média e a idade mais alta.
    Exemplos:
    >>> idade_media(10,20,30,40)
    25.0
    >>> idade_media(5,10,15,20)
    12.5
    >>> idade_maior(10,20,30,40)
    40
    >>> idade_maior(20,15,10,5)
    20
    '''
    idade_med = (idade1 + idade2 + idade3 + idade4)/4
    return idade_med

def idade_maior(idade1,idade2,idade3,idade4):
    maior = 0
    if idade1 >= maior:
        maior = idade1
    if idade2 >= maior:
        maior = idade2
    if idade3 >= maior:
        maior = idade3
    if idade4 >= maior:
        maior = idade4

    return maior

def entrada():
    idade1 = float(input('Idade da primeira pessoa: '))
    idade2 = float(input('Idade da segunda pessoa: '))
    idade3 = float(input('Idade da terceira pessoa: '))
    idade4 = float(input('Idade da quarta pessoa: '))
        
    idade_med = idade_media(idade1,idade2,idade3,idade4)
    maior = idade_maior(idade1,idade2,idade3,idade4)    
        
    
    print(f'-------------------\nIdade Média = {idade_med}')
    print(f'Idade Maior = {maior}')

entrada()