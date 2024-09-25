## Simulated Annealing: Knapsack Problem & N-Queens Problem

### Descrição Geral
Este projeto consiste em duas implementações do algoritmo de **Simulated Annealing** (ou **Resfriamento Simulado**) para resolver dois problemas clássicos de otimização: o **Problema da Mochila (Knapsack)** e o **Problema das N-Rainhas (N-Queens)**. Simulated Annealing é um algoritmo de busca global que simula o processo físico de resfriamento gradual de materiais para encontrar soluções ótimas ou quase ótimas em problemas complexos.

### 1. Simulated-Annealing /knapsack.py: Problema da Mochila

#### Descrição
O problema da mochila envolve uma mochila com um limite de peso, e um conjunto de itens, cada um com um peso e um valor. O objetivo é encontrar uma combinação de itens que maximize o valor total sem exceder o limite de peso da mochila.

#### Estrutura do Código
- **Item:** Uma classe que define um item com peso (`weight`) e valor (`value`).
- **Knapsack:** Classe que representa o problema, contendo o número de itens, a lista de itens, a solução (representada como uma lista de binários), e o peso máximo da mochila.
- **Funções:**
  - `create_knapsack_problem_instance`: Cria uma instância do problema da mochila com itens gerados aleatoriamente.
  - `set_initial_state`: Define um estado inicial para a solução, onde cada item tem uma probabilidade de ser incluído na mochila.
  - `objective`: Calcula o valor total da mochila e penaliza soluções que ultrapassam o peso máximo.
  - `get_random_neighbour_state`: Gera um estado vizinho modificando aleatoriamente a inclusão ou exclusão de um item.
  - `get_initial_temperature`: Calcula a temperatura inicial para o processo de resfriamento baseado em uma média de valores obtidos de estados vizinhos.
  - `simulated_annealing`: Implementa o algoritmo de Simulated Annealing, que ajusta a solução atual para minimizar o custo (penalização) e maximizar o valor.

#### Como Executar
O código gera uma instância do problema da mochila com 50 itens e um peso máximo de 500 unidades. Ele aplica o algoritmo de Simulated Annealing para encontrar uma solução otimizada. Ao final, exibe os itens que foram adicionados ou não à mochila, além do peso total acumulado.

#### Saída Esperada
- Itens que não foram adicionados.
- Itens que foram adicionados à mochila, juntamente com seu peso e valor.
- Peso total dos itens selecionados.

### 2. Simulated-Annealing /nqueens.py: Problema das N-Rainhas

#### Descrição
O problema das N-rainhas consiste em posicionar N rainhas em um tabuleiro de xadrez de N x N, de modo que nenhuma rainha possa atacar outra, ou seja, não pode haver duas rainhas na mesma linha, coluna ou diagonais.

#### Estrutura do Código
- **NQueens:** Classe que representa o problema, contendo o número de rainhas e a solução (representada como uma lista de inteiros onde o índice representa a coluna e o valor no índice representa a linha em que a rainha está posicionada).
- **Funções:**
  - `create_nqueens_problem_instance`: Cria uma instância do problema com o número especificado de rainhas.
  - `set_initial_state`: Define um estado inicial aleatório para o posicionamento das rainhas.
  - `objective`: Calcula o número de conflitos em uma solução, ou seja, o número de ataques entre rainhas.
  - `get_random_neighbour_state`: Gera um estado vizinho alterando a posição de uma rainha em uma coluna aleatória.
  - `get_initial_temperature`: Calcula a temperatura inicial para o processo de resfriamento com base na média de valores de estados vizinhos.
  - `simulated_annealing`: Implementa o algoritmo de Simulated Annealing, ajustando a solução para minimizar o número de conflitos entre as rainhas.

#### Como Executar
O código cria uma instância do problema das 8 rainhas e aplica o algoritmo de Simulated Annealing para encontrar uma solução com o mínimo número possível de conflitos.

#### Saída Esperada
- A solução final (posicionamento das rainhas no tabuleiro).
- Estrutura da instância da classe `NQueens`, com o número de rainhas e a solução final.

### Como Funciona o Simulated Annealing
1. **Estado Inicial:** Começa com uma solução inicial (que pode ser gerada aleatoriamente).
2. **Estado Vizinho:** A cada iteração, o algoritmo faz pequenas alterações no estado atual (gerando um vizinho).
3. **Objetivo:** Avalia a qualidade do estado com base na função objetivo (quantidade de conflitos no N-Queens ou valor/peso no Knapsack).
4. **Aceitação de Mudanças:** Se o estado vizinho for melhor, ele é aceito. Se for pior, ele pode ser aceito com uma probabilidade baseada na temperatura atual e na diferença entre os estados.
5. **Resfriamento:** A temperatura diminui gradualmente, reduzindo a probabilidade de aceitar soluções piores conforme o algoritmo avança.

### Como Rodar os Arquivos
1. Clone ou faça o download deste repositório.
2. Execute os scripts em um ambiente Python:

   Para o problema da mochila:
   ```bash
   python knapsack.py
   ```

   Para o problema das N-rainhas:
   ```bash
   python nqueens.py
   ```

Ambos os scripts foram projetados para rodar com o Python 3.x e requerem a biblioteca `dataclasses`.
