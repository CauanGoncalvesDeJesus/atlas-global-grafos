# E1 — Proposta e Definição do Projeto

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 19 de março de 2026  
> **Peso:** 10% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | |
| Integrante 1 | Gabriel Nascimento de Souza —  39130819|
| Integrante 2 | Lucas Marins de Souza Oliveira — 47992603 |
| Integrante 3 | Cauan Goniçalves de jesus — RA |
| Domínio de aplicação | Busca e resgate, logística de emergência e apoio à decisão  |

---

## 1. Contexto e Motivação

> Descreva o problema do mundo real que será abordado. Por que ele é relevante?  
> *Orientação: 2 a 3 parágrafos. Seja específico — evite generalizações.*

<!-- A gente escolheu esse tema com foco em operações de busca e resgate, principalmente em áreas isoladas, trilhas, regiões rurais ou locais com acesso comprometido, a escolha do caminho interfere diretamente no tempo de resposta da equipe. Em muitos casos, a decisão precisa ser tomada com pressão, pouca visibilidade do terreno e informações incompletas. Quando isso acontece, a definição da rota acaba sendo feita no improviso, o que pode aumentar o risco da operação e atrasar a chegada ao ponto onde a vítima foi vista pela última vez. 

O problema central deste projeto é justamente reduzir esse improviso. Nem sempre o caminho aparentemente mais curto é o melhor: um trecho pode ter maior dificuldade, apresentar obstáculos, passar por uma área de risco ou consumir mais tempo do que outra rota com mais etapas. Por isso, a análise precisa considerar não apenas a ligação entre os pontos, mas também o custo associado a cada trajeto. 

Diante desse cenário, o projeto propõe um sistema capaz de representar uma área de resgate como um grafo e indicar a rota mais adequada entre uma origem e um destino. A proposta é relevante porque transforma um problema real de deslocamento em uma solução estruturada, mensurável e justificável.  --> 

---

## 2. Objetivo Geral

> O que o sistema deve ser capaz de fazer ao final?  
> *Orientação: 1 frase clara e objetiva. Ex.: "O sistema deve calcular a rota de menor custo entre dois pontos em um mapa urbano."*

<!-- Desenvolver um sistema capaz de carregar, por arquivo, um mapa de resgate representado como grafo e calcular a rota de menor custo entre dois pontos, utilizando o algoritmo de Dijkstra.  -->

---

## 3. Objetivos Específicos

> Desmembre o objetivo geral em metas mensuráveis.  
> *Orientação: liste entre 3 e 5 itens. Cada item deve ser verificável — use verbos como "implementar", "calcular", "exibir", "carregar".*

- [mplementar a leitura de um grafo por arquivo JSON. ] 
- [Representar a área de resgate por meio de uma lista de adjacência. ] 
- [Permitir a seleção do vértice de origem e do vértice de destino.  ] 
- [Exibir o caminho encontrado e o custo total da rota. ] 

---

## 4. Público-Alvo / Caso de Uso Principal

> Para quem ou em qual cenário o sistema seria utilizado?  
> *Orientação: descreva um cenário concreto de uso. Ex.: "Um entregador de aplicativo que precisa otimizar a sequência de entregas em um bairro."*

<!-- O sistema é voltado para equipes de busca e resgate, brigadistas, defesa civil, bombeiros ou grupos que atuem em operações de localização em ambientes de difícil acesso. Em um cenário prático, a equipe parte de uma base de resgate e precisa alcançar um abrigo, o último ponto conhecido ou o local provável da vítima com a melhor rota disponível no momento. 

Na versão inicial do projeto, o caso de uso principal será a simulação dessas operações a partir de mapas previamente cadastrados em arquivo. O usuário escolherá o ponto de origem e o de destino, e o sistema exibirá o caminho encontrado junto com o custo total, ajudando na visualização da decisão tomada pelo algoritmo.  -->

---

## 5. Justificativa Técnica — Por que Grafos?

> Por que a modelagem em grafo é a abordagem mais adequada para este problema?  
> *Orientação: explique quais elementos do problema mapeiam naturalmente para vértices e arestas. Mencione se há pesos, direção, ou restrições que reforçam a escolha.*

<!--A gente vai usr a modelagem em grafo pois é a mais adequada porque os elementos do problema se encaixam de forma natural nessa estrutura. Os pontos relevantes da área, como base, trilhas, abrigo, áreas de risco, último ponto conhecido e destino, podem ser representados por vértices. Já os caminhos possíveis entre esses pontos podem ser representados por arestas. 

Como cada ligação possui um custo associado, o grafo precisa ser ponderado. Esse peso poderá representar distância, tempo estimado ou dificuldade do trajeto, dependendo da configuração adotada. Com essa estrutura, torna-se possível aplicar algoritmos clássicos de caminho mínimo. O algoritmo de Dijkstra foi escolhido porque atende bem ao objetivo inicial do sistema em grafos com pesos não negativos, permitindo encontrar a melhor rota de forma clara, objetiva e coerente com a proposta do projeto.  -->

---

## 6. Tipo de Grafo

> Especifique as características do grafo que o problema requer.

| Característica | Escolha | Justificativa breve |
|----------------|---------|---------------------|
| Dirigido ou não-dirigido |Não-dirigido  | Na primeira versão, os caminhos poderão ser percorridos nos dois sentidos.|

| Ponderado ou não-ponderado | Ponderado | Cada aresta possui um custo associado, como tempo, distância ou dificuldade.|

| Conectado / bipartido / geral | Conectado e geral |Os pontos precisam estar ligados para permitir o cálculo de rotas entre origem e destino. |

| Representação interna pretendida | lista de adjacência / matriz |É mais prática e eficiente para trabalhar com vizinhos e pesos em grafos esparsos.  |

---

## 7. Diagrama Conceitual

> Insira aqui ao menos uma figura que ilustre o domínio do problema.  
> *Pode ser uma imagem exportada do Draw.io, Excalidraw, foto de esboço à mão etc.*  

![Diagrama Conceitual](atlas_diagrama.png)

** Base de Resgate, Trilha A, Trilha B, Abrigo/Objetivo, Área de Risco, Último Ponto Conhecido e Destino/Vítima são representados como vértices. Os números nas conexões indicam o peso das arestas, que pode representar tempo, distância ou dificuldade do percurso. ** 

---

## Checklist de Entrega

Antes de submeter, confirme:

- [ ] Texto entre 300 e 600 palavras (seções 1 a 5)
- [ ] Todos os campos da tabela de identificação preenchidos
- [ ] Tipo de grafo especificado com justificativa
- [ ] Diagrama presente e referenciado no texto
- [ ] Arquivo nomeado como `E1_NomeGrupo_Grafos.docx` (versão Word) ou PR aberto (versão GitHub)

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
