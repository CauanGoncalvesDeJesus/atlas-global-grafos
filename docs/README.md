# Atlas Global Grafos

Sistema desenvolvido para a disciplina de Teoria dos Grafos com foco em cálculo de rotas inteligentes para cenários de emergência e desastres naturais.

O projeto utiliza algoritmos de grafos como Dijkstra e BFS para encontrar caminhos entre pontos estratégicos no mapa.

---

# Funcionalidades

* Representação de grafos
* Algoritmo de Dijkstra
* Busca em largura (BFS)
* Interface web com Flask
* Visualização de rotas
* Leitura de dados via JSON

---

# Tecnologias Utilizadas

* Python 3
* Flask
* HTML5
* CSS3
* JSON

---

# Estrutura do Projeto

```text
atlas-global-grafos/
├── data/
│   └── grafo.json
├── docs/
│   ├── E1_Template.md
│   ├── E2_Template.md
│   ├── E3_Template.md
│   └── README.md
├── src/
│   ├── algorithms/
│   │   ├── bfs.py
│   │   └── dijkstra.py
│   ├── core/
│   │   ├── edge.py
│   │   └── graph.py
│   └── io/
│       └── reader.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── tests/
│   └── test_graph.py
├── main.py
├── README.md
└── .gitignore
```

---

# Pré-requisitos

Antes de executar o projeto, instale:

* Python 3.10+
* pip

Verifique a instalação:

```bash
python --version
pip --version
```

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/atlas-global-grafos.git
```

Entre na pasta do projeto:

```bash
cd atlas-global-grafos
```

Instale as dependências:

```bash
pip install flask
```

---

# Como Executar o MVP

Execute o sistema com:

```bash
python main.py
```

Após iniciar, abra no navegador:

```text
http://127.0.0.1:5000
```

---

# Funcionamento

O sistema permite visualizar rotas entre pontos estratégicos utilizando algoritmos de grafos.

## Dijkstra

Calcula o menor caminho considerando pesos entre vértices.

Complexidade:

```text
O((V + E) log V)
```

## BFS

Realiza busca em largura considerando o menor número de conexões.

Complexidade:

```text
O(V + E)
```

---

# Arquivo de Dados

Os dados do grafo estão em:

```text
data/grafo.json
```

O arquivo contém:

* vértices
* conexões
* pesos das arestas
* localizações

---

# Testes

Estrutura de testes localizada em:

```text
tests/
```

Para executar:

```bash
pytest tests/
```

---

# Interface

## Tela Inicial

* seleção de rotas
* visualização dos pontos
* escolha do algoritmo

## Tela de Resultado

* exibição do menor caminho
* custo total da rota
* caminho percorrido

---

# Integrantes

* Gabriel
* Lucas
* Cauan
---

# Disciplina

Teoria dos Grafos
Profa. Dra. Andréa Ono Sakai
