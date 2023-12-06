from dataclasses import dataclass

'''
- Receber um valor em minutos
- Usar um campo composto para verificar quantas horas esse minutos equivalem
- Retorna essa relação de horas e minutos
'''
@dataclass
class Tempo:
    horas : int
    minutos : int 

def calcularHoras(minutos: int) -> Tempo:
    '''
    Exemplos:
    >>> calcularHoras (100)
    Tempo(horas=1, minutos=40)
    >>> calcularHoras(350)
    Tempo(horas=5, minutos=50)

    '''
    tempo = Tempo(0,0)
    tempo.horas = minutos // 60
    tempo.minutos = minutos % 60

    return tempo

def entrada():
    minutos = int(input('Informe os minutos: '))
    tempoSaida = calcularHoras(minutos)
    print(tempoSaida.horas)
    print(tempoSaida.minutos)

entrada()