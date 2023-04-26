def maior_q_ou_igual_acinco(matriz):
    return len(matriz) >= 5

def produto_matriz(matriz):
    maior_linha = 0
    for linha in matriz:
        valor = 1
        for numero in linha:
            valor = valor * numero
        if valor >= maior_linha:
            maior_linha = valor
    
    maior_coluna = 1
    maior_coluna_list = [[x[y] for x in matriz] for y in list(range(len(matriz)))]
    for linha in maior_coluna_list:
        valor = 1
        for numero in linha:
            valor = valor * numero
        if valor >= maior_coluna:
            maior_coluna = valor
    
    lista_diagonal = [linha[linha[linha.index]] for linha in matriz]
    diagonal = 1
    for numero in lista_diagonal:
        diagonal = diagonal * numero
            
    return linha_produto