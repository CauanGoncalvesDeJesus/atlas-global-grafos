from collections import deque

def calcular_bfs(grafo, inicio, fim):
    """
    Busca em Largura (BFS) para encontrar a rota com menos conexões.
    """
    fila = deque([(inicio, [inicio])])
    visitados = {inicio}

    while fila:
        (vertice_atual, caminho) = fila.popleft()

        for vizinho in grafo[vertice_atual]:
            if vizinho == fim:
                final_path = caminho + [vizinho]
                return final_path, len(final_path) - 1 # Custo é o nº de arestas
            
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return [], float('inf')
