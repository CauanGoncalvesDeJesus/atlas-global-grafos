import json
from flask import Flask, render_template, jsonify
from src.algorithms.dijkstra import calcular_dijkstra
from src.algorithms.bfs import calcular_bfs

app = Flask(__name__)

def carregar_dados():
    try:
        with open('data/grafo.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        grafo_processado = {v['id']: v for v in dados['vertices']}
        
        adjacencias = {v['id']: {} for v in dados['vertices']}
        for a in dados['arestas']:
            adjacencias[a['origem']][a['destino']] = a['peso']
            
        return grafo_processado, adjacencias
    except Exception as e:
        print(f"Erro ao carregar grafo.json: {e}")
        return {}, {}


DADOS_NOS, GRAFO_ADJACENCIA = carregar_dados()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route/<method>/<support>/<call>/<disaster>')
def get_sar_route(method, support, call, disaster):
    try:
        algoritmo = calcular_dijkstra if method == 'dijkstra' else calcular_bfs

        rota_a, custo_a = algoritmo(GRAFO_ADJACENCIA, support, call)
        rota_b, custo_b = algoritmo(GRAFO_ADJACENCIA, call, disaster)

        caminho_final = rota_a + rota_b[1:]
        custo_total = custo_a + custo_b

        path_coords = [
            {"lat": DADOS_NOS[no]['lat'], "lng": DADOS_NOS[no]['lng']} 
            for no in caminho_final
        ]

        return jsonify({
            "path": path_coords,
            "total_cost": f"{custo_total:.2f} min" if method == "dijkstra" else f"{custo_total} conexões"
        })

    except Exception as e:
        return jsonify({"error": f"Falha no motor ATLAS: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
