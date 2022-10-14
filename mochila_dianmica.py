valores = [4, 2, 10, 2, 1]
pesos = [12, 2, 4, 1, 1]
capacidade = 15
aux = len(valores)
elements = []


def mochilaDinamica(capacidade,pesos,valores,tam):
    # "m" é o dicionário que irá conter os dados
    m = {} 
    
    for i in range(capacidade+1):
        m[(0,i)] = 0

    # Iterar sobre as linhas
    for i in range(1,aux + 1):
        # Iterar sobre as colunas
        for w in range(capacidade + 1):
            # Se o peso do item pesa menos que o peso daquela coluna o valor 
            # a chave e o valor passam a ser ou o valor da linha anterior ou
            # o valor resultante da soma do valor da linha anterior somado 
            # ao peso dos valores. 
            if pesos[i - 1] <= w:
                m[(i,w)] = max(m[(i - 1,w)], valores[i - 1] + m[(i-1,w-pesos[i - 1])])
            else:
                # A entrada no dicionário se torna o valor da linha anterior
                m[(i,w)] = m[(i-1,w)]

    # Enquanto a capacidade for maior ou igual a zero
    # os pesos que formam determinados para o dicionario
    # serao adicionados a uma lista auxiliar para serem 
    # printados          
    c = capacidade
    for i in range(aux, 0, -1):
        if c - pesos[i - 1] < 0:
            continue
        if m[i, c] - m[i - 1, c - pesos[i - 1]] == valores[i - 1]:
            elements.append(i)
            c -= pesos[i - 1]            
    
    # Print da lista dos elementos presentes - 1 
    print(elements)        

    return m[(aux,capacidade)]    
                                 
                
print(mochilaDinamica(capacidade,pesos,valores,aux))
