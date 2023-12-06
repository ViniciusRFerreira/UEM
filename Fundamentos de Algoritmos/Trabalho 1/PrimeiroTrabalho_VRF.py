#Vinicius R. Ferreira

def totaliza_pedidos(pedidos):
    '''
    Produz uma estrutura que totaliza a demanda de cada produto
    a partir de *pedidos*.
    '''
    totalizacao = []
    totalizacao.append('Bobina')
    totalizacao.append(0)
    totalizacao.append('Chapa')
    totalizacao.append(0)
    totalizacao.append('Painel')
    totalizacao.append(0)

    x = len(pedidos)
    for i in range(0,x,2):
        for j in range(0,x,2):
            if pedidos[i] == pedidos[j]:
                if pedidos[i] == 'Bobina':
                    totalizacao[1] += pedidos[i+1]
                    pedidos[i+1] = 0
                elif pedidos[i] == 'Chapa':
                    totalizacao[3] += pedidos[i+1]
                    pedidos[i+1] = 0
                elif pedidos[i] == 'Painel':
                    totalizacao[5] += pedidos[i+1]
                    pedidos[i+1] = 0
    print(f' - Pedidos Únicos: {totalizacao}')
    return totalizacao                
            


def ha_ruptura(totalizacao):   
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos com ruptura do estoque.
    '''
    ruptura = []
    estoque = []

    estoque.append('Papel')     #[0]
    estoque.append(100000)      #[1]
    estoque.append(50.0)        #[2]
    estoque.append(60.0)        #[3]

    estoque.append('Papelão')   #[4]
    estoque.append(50000)       #[5]
    estoque.append(40.0)        #[6]
    estoque.append(48.0)        #[7]

    estoque.append('Painéis')   #[8]
    estoque.append(30000)       #[9]
    estoque.append(75.0)        #[10]
    estoque.append(90.0)        #[11]
    print(f' - Estoque: {estoque}')

    if totalizacao[1] > estoque[1]:
        ruptura.append(f'{totalizacao[0]} de Papel')

    if totalizacao[3] > estoque[5]:
        ruptura.append(f'{totalizacao[2]} de Papelão')

    if totalizacao[5] > estoque[9]:
        ruptura.append(f'{totalizacao[4]} de Madeira')

    print(f' - Ruptura: {ruptura}')
    return estoque


def relatorio_vendas(totalizacao,vendedor,desconto,estoque,pedidos2):
    receita = 0
    custo = 0
    j = 0
    lista = []
    for i in range(0,len(pedidos2),2):
        receita_individual = 0
        custo_individual = 0
    
        if pedidos2[i] == 'Bobina':
            
            receita_individual = pedidos2[i+1]*(estoque[3] - (estoque[3]*(desconto[j]/100)))
            receita += pedidos2[i+1]*(estoque[3] - (estoque[3]*(desconto[j]/100)))
            
            custo_individual = pedidos2[i+1]*(estoque[2])
            custo += pedidos2[i+1]*(estoque[2])
            j += 1
            

        elif pedidos2[i] == 'Chapa':
            receita_individual = pedidos2[i+1]*(estoque[7] - (estoque[7]*(desconto[j]/100)))
            receita += pedidos2[i+1]*(estoque[7] - (estoque[7]*(desconto[j]/100)))

            custo_individual = pedidos2[i+1]*(estoque[6])
            custo += pedidos2[i+1]*(estoque[6])
            j += 1


        elif pedidos2[i] == 'Painel':
            receita_individual = pedidos2[i+1]*(estoque[11] - (estoque[11]*(desconto[j]/100)))
            receita += pedidos2[i+1]*(estoque[11] - (estoque[11]*(desconto[j]/100)))

            custo_individual = pedidos2[i+1]*(estoque[10])
            custo += pedidos2[i+1]*(estoque[10])
            j += 1


        lucro_individual = receita_individual - custo_individual
        vendedor[i+1] = lucro_individual
    print(vendedor)
    x = len(vendedor)
    for i in range(0,x,2):
        for j in range(0,x,2):
            if vendedor[i] == vendedor[j] and i != j:
                vendedor[i+1]+=vendedor[j+1]
                vendedor[j] = 0
                vendedor[j+1] = 0
    print(vendedor)
    

    lucro_liquido = receita - custo
    return lucro_liquido
    

def entrada():
    pedidos = []
    desconto = []
    pedidos2 = []
    vendedor = []
    prod = 1
    while prod != 0:

        

        prod = int(input('\n1 - Bobina\n2 - Chapa\n3 - Painel\n0 - Encerrar Adição\n\n'))
        
        if prod < 0 or prod > 3:
            print(' - Erro, informe um produto válido da lista.')
        else:
            
            if prod == 0:
                print('\n - Encerrada adição.\n')
                break
            
            if prod == 1:
                prod_mostra = 'Bobina'
            elif prod == 2:
                prod_mostra = 'Chapa'
            else:
                prod_mostra = 'Painel'
            
            pedidos.append(prod_mostra)

            quant = int(input(f'\nInforme a quantidade de {prod_mostra} vendidas: '))
            
            if quant > 0:
                pedidos.append(quant)
            else:
                print('\n - Informe um valor válido de quantidade dos produtos vendidos.')
            
            vendedor.append(input('\nNome do Vendedor: '))
            vendedor.append(0)

            desconto.append(float(input('\nDesconto %: ')))
    
    print(f' - Pedidos: {pedidos}')

    for i in range(0,len(pedidos)):
        pedidos2.append(pedidos[i])
    
    print(vendedor)

    totalizacao = totaliza_pedidos(pedidos)

    estoque = ha_ruptura(totalizacao)
    
    saida = relatorio_vendas(totalizacao,vendedor,desconto,estoque,pedidos2)
    print(f' - Lucro Líquido: R$ {saida}')


entrada()

#Vinicius R. Ferreira