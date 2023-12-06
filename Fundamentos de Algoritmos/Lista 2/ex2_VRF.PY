'''
- Receber valores de entrada (ra, nome e curso) de um aluno
- Cadastrar as informações e atribuir a um dado composto
- Retornar a estrutura cadastrada
'''
from dataclasses import dataclass
@dataclass
class Aluno:
    ra:int
    nome:str
    curso:str

def cadastro(ra:int,nome:str,curso:str):
    '''
    Exemplos:
    >>> cadastro(120,'Gabriel','Artes')
    Aluno(ra=120, nome='Gabriel', curso='Artes')
    >>> cadastro(130,'Vinicius','Ciências da Computação')
    Aluno(ra=130, nome='Vinicius', curso='Ciências da Computação')
    '''
    nome_aluno = Aluno(ra, nome, curso)
    return nome_aluno


def informacoes():
    ra = int(input('Informe o ra: '))
    nome = input('Informe seu nome: ')
    curso = input('Informe seu curso: ')

    info = cadastro(ra,nome, curso)
    mostrarDados(info)


def mostrarDados(aluno : Aluno):
    print(aluno.ra)
    print(aluno.nome)
    print(aluno.curso)

informacoes()