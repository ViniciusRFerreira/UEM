def somatorio_alternativas(s):
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    alternativas = []
    alternativa = 1
    while s > 0:
    # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
            
        # divide todas as alternativas que compõe 
        # o somatório s por 2
        s = s // 2

        # procura a próxima alternativa
        alternativa = alternativa * 2
    #print(alternativas)
    return alternativas

def desempenho(codigo,redacao,respostas):
    '''
    Algoritmo que recebe um código de participante, uma nota de redação e as respostas das questões, retornando no final o código do participante e a nota final dele, sendo que redação = 0 é desclassificado.
    Exemplos:
    >>> desempenho([3211,7102,1234,5812,9123],[80,0,90,32,0],[[4,10,4,16,10],[1,2,3,4,5],[21,8,8,8,14],[20,0,8,16,1],[5,4,3,2,1]])
    [[1234, 109.5], [3211, 97.0], [5812, 49.5]]
    >>> desempenho([321,102,234,812,999],[40,10,0,22,56],[[2,1,15,16,10],[1,2,8,4,10],[21,8,6,4,3],[2,1,4,31,1],[6,16,12,2,4]])
    [[102, 24.0], [321, 49.0], [812, 23.5], [999, 57.5]]
    '''
    gabarito = [21,10,8,16,15]
    lista = []
    matriz = []
    
    for l in range(len(respostas)):
        nota = 0
        if redacao[l] > 0:
            if codigo[l] not in lista:
                lista.append(codigo[l])
                for c in range(5):
                    lista_resp = somatorio_alternativas(respostas[l][c])
                    lista_gabarito = somatorio_alternativas(gabarito[c])
                    nota += nota_questao(lista_resp,lista_gabarito)

                lista.append(redacao[l]+nota)      
                matriz.append(lista)
                lista = []
                        
        elif len(codigo) == 1:
            matriz.append(lista)
            print(matriz)

    return sorted(matriz)


def nota_questao(lista_resp,lista_gabarito):
    soma = 0
    x = len(lista_resp)
    for i in range(len(lista_resp)):
        if lista_resp[i] in lista_gabarito:
            soma += 1

    if set(lista_resp) == set(lista_gabarito):
        return 6.0
    elif x == soma:
        pontos = somatoria(lista_resp,lista_gabarito)
        return pontos
    else:
        return 0.0
        
    

def somatoria(lista_resp,lista_gabarito):
    qtd_certas = len(lista_gabarito)
    if qtd_certas == 2:
        return 3.0*len(lista_resp)
    elif qtd_certas == 3:
        return 2.0*len(lista_resp)
    elif qtd_certas == 4:
        return 1.5*len(lista_resp)
    elif qtd_certas == 5:
        return 1.2*len(lista_resp)


def entrada():
    codigo = []
    redacao = []
    respostas = []
    resposta = []
    x = True
    while x == True:
        cod = int(input('\nCódigo do candidato: '))
        if cod > 0 and cod not in codigo:
            codigo.append(cod)
            red = float(input('\nRedação: '))
            if red >= 0:
                redacao.append(red)
                for i in range(5):
                    resp = int(input(f'\n{i+1}ª questão: '))
                    resposta.append(resp)

                respostas.append(resposta)
                resposta = []

            else:
                print('\n - Erro, nota de redação inválida.')
                break
        else:
            print('\n - Informe um código de candidato válido!')

        y = input('\n - Pressione "ENTER" para continuar a adição. ')
        if y != '':
            x == False
            break

    nota_alunos = desempenho(codigo,redacao,respostas)
    return nota_alunos        

nota_alunos = entrada()
print(f'\n{nota_alunos}')


#Vinicius R. Ferreira