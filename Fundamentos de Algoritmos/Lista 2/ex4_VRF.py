'''
- Recebendo o nome de uma pessoa
- Executando o código e verificando a quantidade de letras para comparar e verificar o tamanho do nome
- Retorna o tamanho do nome de acordo com sua quantidade de letras
'''
from enum import Enum, auto
from dataclasses import dataclass

@dataclass
class Nome(Enum):
    CURTO = auto()
    LONGO = auto()
    MEDIANO = auto()

def quantidadeLetras(nome):
    '''
    Exemplos:
    >>> quantidadeLetras('Vinicius')
    'MEDIANO'
    >>> quantidadeLetras('Joao')
    'CURTO'
    >>> quantidadeLetras('Bernadete')
    'LONGO'
    '''
    val = len(nome)
    if val <= 4:
        nome_saida = Nome.CURTO.name
    elif val > 8:
        nome_saida = Nome.LONGO.name
    else: 
        nome_saida = Nome.MEDIANO.name
    return nome_saida

def entrada():
    nome = input('Informe um nome: ')
    tamanhoNome = quantidadeLetras(nome)
    print(tamanhoNome)

entrada()