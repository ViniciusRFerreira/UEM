'''
- Receber a cor atual do semáforo
- E mostrar qual a próxima cor
'''
from enum import Enum, auto
from dataclasses import dataclass

class Cor(Enum):
    '''programa para retornar próxima cor do semaforo
    Exemplos:
    >>> prox_cor('VERDE')
    <Cor.AMARELO: 2>
    >>> prox_cor('AMARELO')
    <Cor.VERMELHO: 3>
    >>> prox_cor('VERMELHO')
    <Cor.VERDE: 1>
    '''
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()

def prox_cor(cor_atual):
    if cor_atual == 'VERDE':
        prox_cor = Cor.AMARELO
    elif cor_atual == 'AMARELO':
        prox_cor = Cor.VERMELHO
    else:
        prox_cor = Cor.VERDE
    return prox_cor


def entrada():
    cor = input('Qual a cor atual? \n 1 - Verde\n 2 - Amarelo\n 3 - Vermelho\n---------------\n')
    if cor == '1':
        cor_atual = 'VERDE'
    elif cor == '2':
        cor_atual = 'AMARELO'
    else:
        cor_atual = 'VERMELHO'

    saida = prox_cor(cor_atual)
    print(saida)

entrada()