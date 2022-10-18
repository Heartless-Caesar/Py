valores = [4, 2, 10, 2, 1]
pesos = [12, 2, 4, 1, 1]
capacidade = 15
aux = len(valores)
elements = []

def mochilaDinamica(capacidade,pesos,valores,tam):
    m = {} 
    
    for i in range(capacidade+1):
        m[(0,i)] = 0

    for i in range(1,aux + 1):
        
        for w in range(capacidade + 1):
             
            if pesos[i - 1] <= w:
                m[(i,w)] = max(m[(i - 1,w)], valores[i - 1] + m[(i-1,w-pesos[i - 1])])
            else:
                m[(i,w)] = m[(i-1,w)]
         
    c = capacidade
    for i in range(aux, 0, -1):
        if c - pesos[i - 1] < 0:
            continue
        if m[i, c] - m[i - 1, c - pesos[i - 1]] == valores[i - 1]:
            elements.append(i)
            c -= pesos[i - 1]            
    
    print(elements)        

    return m[(aux,capacidade)]    
                                 
                
print(mochilaDinamica(capacidade,pesos,valores,aux))
