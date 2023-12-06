'''
- Algoritimo para receber votos de uma eleição e retornar o candidato eleito ou se será necessário uma nova eleição.
'''
def votos(lista):
    '''
    Exeplos:
    >>> votos([1,1,1,1,2,2,0,0])
    ('Candidato 1', 50.0, 25.0)
    >>> votos([2,2,2,2,1,0])
    ('Candidato 2', 66.67, 16.67)
    '''
    cand1 = 0
    cand2 = 0
    branco = 0

    for i in range(len(lista)):
        if lista[i] == 1:
            cand1 += 1
        elif lista[i] == 2:
            cand2 +=1
        else:
            branco += 1

    total = len(lista)
    brancos = (branco * 100)/total

    if (len(lista)/2) <= branco:
        eleito = 'branco'
        return 'Novas eleições serão convocadas',round(eleito,2),round(brancos,2)
    elif cand1 > cand2 and cand1 >= branco:
        eleito = (cand1 * 100)/total
        return 'Candidato 1',round(eleito,2),round(brancos,2)
    elif cand2 > cand1 and cand2 >= branco:
        eleito = (cand2 * 100)/total
        return 'Candidato 2',round(eleito,2),round(brancos,2)
    else:
        return 'Empate',round(eleito,2),round(brancos,2)
    

def entrada():
    voto = 4
    lista = []
    while voto != 3 and voto >= 0:
        voto = int(input('\n1 - "Candidato 1" \n2 - "Candidato 2" \n0 - "Branco ou Nulo"\n3 - "Encerrar Operação"\n\n'))
        lista.append(voto)

        saida,eleito,brancos = votos(lista)

        if saida == 'Novas eleições serão convocadas':
            print(f'\n - A quantidade de valores em branco foi igual a {round(brancos,2)}%, então novas eleições serão convocadas.\n')
        elif saida == 'Candidato 1':
            print(f'\n - O candidato 1 foi eleito com {round(eleito,2)}% dos votos.\n')
        elif saida == 'Candidato 2':
            print(f'\nO candidato 2 foi eleito com {round(eleito,2)}% dos votos.\n')
        else:
            print('\n - Empate, eleições vão ao segundo turno.\n')