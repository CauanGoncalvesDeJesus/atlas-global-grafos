import heapq

def calcular_dijkstra(grafo, inicio, fim):
    """
    Implementação do algoritmo de Dijkstra para o ATLAS Global.
    Retorna o caminho mais curto e o custo total acumulado.
    """
    # distancias armazena o menor custo para chegar a cada vértice
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    
    # Fila de prioridade para selecionar o vértice com menor distância atual
    pq = [(0, inicio)]
    predecessores = {vertice: None for vertice in grafo}

    while pq:
        distancia_atual, vertice_atual = heapq.heappop(pq)

        if vertice_atual == fim:
            break

        if distancia_atual > distancias[vertice_atual]:
            continue

        # Relaxação das arestas vizinhas
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = vertice_atual
                heapq.heappush(pq, (distancia, vizinho))

    # Reconstrói o caminho percorrido
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    
    return caminho[::-1], distancias[fim]
