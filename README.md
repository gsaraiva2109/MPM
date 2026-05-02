# MPM - Problema de Corte de Estoque (Cutting Stock Problem)

Este projeto implementa uma solução para o **Problema de Corte de Estoque unidimensional**, utilizando a biblioteca **Google OR-Tools**. O objetivo é minimizar a quantidade de barras de tamanho fixo necessárias para atender a uma demanda de itens com diferentes comprimentos.

## 📋 Descrição do Problema

O projeto resolve o problema clássico de otimização onde:
1. Temos barras brutas de um comprimento padrão (ex: 150m).
2. Temos uma lista de itens com comprimentos específicos e suas respectivas demandas.
3. O objetivo é encontrar a combinação de padrões de corte que minimize o desperdício total de material (ou minimize o número total de barras brutas utilizadas).

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Jupyter Notebook**
- **Google OR-Tools**: Biblioteca para otimização combinatória.
- **Solver SCIP**: Utilizado para resolver o problema de programação inteira.

## 🛠️ Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado. É recomendado o uso de um ambiente virtual ou o Google Colab.

### Instalação

Instale a dependência necessária:

```bash
pip install ortools
```

### Execução

1. Abra o arquivo `main.ipynb` em um ambiente Jupyter (VS Code, JupyterLab, Google Colab).
2. Execute as células sequencialmente.
3. O programa solicitará:
   - Tamanho da barra bruta.
   - Quantidade de tipos de itens.
   - Para cada tipo: Tamanho e Demanda.

## 📊 Estrutura do Código

1. **Entrada de Dados**: Coleta as especificações do problema.
2. **Geração de Padrões**: Gera todos os padrões de corte "maximais" possíveis de forma exaustiva.
3. **Modelagem Matemática**:
   - **Variáveis de Decisão**: Quantidade de vezes que cada padrão de corte é utilizado.
   - **Função Objetivo**: Minimizar o total de barras.
   - **Restrições**: Garantir que a soma dos cortes atenda ou supere a demanda de cada item.
4. **Resolução**: Utiliza o solver SCIP para encontrar a solução ótima.
5. **Resultados**: Exibe as barras utilizadas, o desperdício total e os padrões detalhados.

## 📝 Exemplo de Saída

O código também exporta o modelo matemático no formato LP (Linear Programming) ao final da execução, permitindo a inspeção técnica da formulação.
