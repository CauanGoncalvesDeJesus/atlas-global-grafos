# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto |atlas-global |
| Repositório GitHub |https://github.com/CauanGoncalvesDeJesus/atlas-global-grafos |
| Integrante 1 | Cauan Gonçalves de jesus RGM: 38259788. |
| Integrante 2 | Gabriel Nascimento de Souza RGM : 39130819|
| Integrante 3 |Lucas Marins de Souza Oliveira RGM: 47992603|

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo |Dijkstra |
| Categoria | Algoritmo guloso |
| Complexidade de tempo | O((V + E) log V) |
| Complexidade de espaço |O(V) |
| Problema que resolve |Determinar o menor custo entre origem e destino em um grafo ponderado |

**Por que este algoritmo foi escolhido?**

<!-- O problema central do ATLAS exige encontrar a rota de menor custo entre dois pontos em um ambiente representado como grafo. Como os pesos são não negativos e representam custo de travessia, o Dijkstra resolve exatamente esse cenário com eficiência. -->

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
| Bellman-Ford         | Complexidade maior O(V·E), sendo desnecessário já que não há pesos negativos|

**Limitações no contexto do problema:**

<!-- Não suporta pesos negativos, Trabalha com um único critério de custo (não múltiplos simultaneamente), Requer o grafo totalmente carregado em memória-->

**Referência bibliográfica:**

> <!-- (SKIENA, S. S. The Algorithm Design Manual. 2. ed. Springer, 2008)CORMEN, T. H. et al. Algoritmos: Teoria e Prática. 3. ed. -->

---

### 1.2 Algoritmo Adicional *(se houver)*

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo |BFS |
| Categoria |Busca em largura |
| Complexidade de tempo |O(V + E) |
| Complexidade de espaço |O(V)|

**Justificativa:**

<!--O BFS é utilizado para verificar a alcançabilidade entre vértices, conforme sua propriedade de explorar todos os nós acessíveis a partir da origem. Com base nisso, é possível identificar previamente se existe caminho entre origem e destino antes da execução do Dijkstra. -->

**Referência bibliográfica:**

<!-- CORMEN, T. H. et al. Algoritmos: Teoria e Prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

SKIENA, S. S. The Algorithm Design Manual. 2. ed. Springer, 2008.--> 

---

## 2. Arquitetura em Camadas

> Insira o diagrama abaixo. Pode ser exportado do Draw.io, Excalidraw, etc.

![Diagrama de arquitetura](![alt text](<Atlas Diagrama E2.drawio.png>))

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) |Receber entrada do usuário e exibir resultado da rota | main.py|
| Aplicação (Service) | Coordenar execução do fluxo (validação + algoritmo)|planner.py |
| Domínio (Core) |Representação do grafo e lógica dos algoritmos |graph.py, dijkstra.py |
| Infraestrutura (I/O) |Leitura e interpretação do JSON |file_reader.py |

---

## 3. Estrutura de Diretórios

```
atlas-global-grafos/
├── docs/
├── src/
│   ├── core/
│   │   ├── graph.py
│   │   └── edge.py
│   ├── algorithms/
│   │   ├── dijkstra.py
│   │   └── bfs.py
│   ├── io/
│   │   └── reader.py
│   └── main.py
├── tests/
├── data/
```

> **Justificativa de desvios** *(se houver)*: 
<!--strutura organizada para separar responsabilidades e facilitar testes e manutenção-->
---

## 4. Definição do Dataset

**Formato de entrada aceito:**

<!-- JSON contendo vértices e arestas com pesos representando custo de travessia. -->

**Exemplo de estrutura do arquivo de entrada:**

```json
{
  "vertices": ["base", "trilha_a", "trilha_b", "destino"],
  "arestas": [
    { "origem": "base", "destino": "trilha_a", "peso": 10 },
    { "origem": "trilha_a", "destino": "trilha_b", "peso": 7 },
    { "origem": "trilha_b", "destino": "destino", "peso": 6 }
  ]
}
```

**Estratégia de geração aleatória:**

| Parâmetro | Descrição |
|-----------|-----------|
| Número de vértices | Definido pelo usuário |
| Densidade | Controlada entre 0.0 e 1.0 |
| Faixa de pesos | Entre 1 e 20|

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

| # | Funcionalidade | Prioridade | Critério de aceite |
|---|---------------|------------|-------------------|
| 1 | Leitura de JSON| Alta | Dado um arquivo válido, quando carregado, então o grafo é criado corretamente|
| 2 |Validação do grafo |Alta |Dado dados inválidos, quando processados, então o sistema retorna erro |
| 3 |Execução do Dijkstra |Alta |Dado origem e destino, quando executado, então retorna o menor caminho |
| 4 |Exibição da rota | Média|Dado resultado, quando exibido, então mostra caminho e custo total |
| 5 |Tratamento de “sem rota” |Alta | Dado grafo desconectado, quando consultado, então retorna mensagem adequada|

### 5.2 Out-of-Scope — O que NÃO será feito

| Funcionalidade excluída | Motivo |
|------------------------|--------|
|Interface gráfica |Fora do escopo atual |
| Integração com GPS|Complexidade externa ao projeto |
|Múltiplos critérios de peso |Aumenta complexidade além do necessário |

---

## Checklist de Entrega

- [ ] Big-O de tempo e espaço declarados para cada algoritmo
- [ ] Ao menos 1 alternativa descartada com justificativa
- [ ] Diagrama de arquitetura com 4 camadas identificadas
- [ ] Referência bibliográfica para cada algoritmo (ABNT ou IEEE)
- [ ] Backlog com ≥ 5 itens In-Scope e ≥ 3 Out-of-Scope
- [ ] Ao menos 3 critérios de aceite no formato "dado / quando / então"
- [ ] Exemplo de estrutura de arquivo de entrada presente

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
