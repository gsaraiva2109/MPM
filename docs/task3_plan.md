# Tarefa 3 — Saída Formatada e Integração

**Arquivos:** `output_formatter.py`, `main.py`  
**Dependências:** Tarefas 1 e 2 (para integração final em `main.py`)

---

## Objetivo

Formatar e exibir todos os resultados em português, e orquestrar o pipeline completo
no ponto de entrada do programa.

---

## Implementação — `print_solution()`

Exibe somente os padrões com `x_values[j] > 0` (padrões ativos na solução).

### Formato de saída esperado

```
=== SOLUÇÃO ÓTIMA ===
Status: ÓTIMO

Padrão           | Barras | Desperdício/barra
[1, 1, 0]        |      3 |                10
[0, 2, 1]        |     50 |                20
------------------------------------------------
Total de barras utilizadas : 53
Desperdício total          : 1030 m
Valor objetivo             : 1030.0
```

### Lógica

```python
def print_solution(solution, item_sizes, bar_length):
    status = solution["status"]
    patterns = solution["patterns"]
    x_values = solution["x_values"]

    print("\n=== SOLUÇÃO ÓTIMA ===")
    print(f"Status: {status}\n")

    if status == "INVIÁVEL":
        print("[AVISO] O problema não possui solução viável com os dados fornecidos.")
        return

    # cabeçalho da tabela
    print(f"{'Padrão':<20} | {'Barras':>6} | {'Desperdício/barra':>17}")
    print("-" * 50)

    for j, pat in enumerate(patterns):
        if x_values[j] == 0:
            continue
        waste_j = compute_waste(pat, item_sizes, bar_length)
        print(f"{str(pat):<20} | {x_values[j]:>6} | {waste_j:>17}")

    print("-" * 50)
    print(f"Total de barras utilizadas : {solution['total_bars']}")
    print(f"Desperdício total          : {int(solution['total_waste'])} m")
    print(f"Valor objetivo             : {solution['objective_value']}")
```

> **Atenção:** importar `compute_waste` de `pattern_generator` para calcular o
> desperdício por barra na tabela.

---

## Implementação — `print_patterns_table()`

Lista todos os padrões enumerados (não apenas os usados), útil para o relatório.

### Formato de saída esperado

```
=== PADRÕES VIÁVEIS ENUMERADOS ===
Total: 15 padrões

Índice | Padrão        | Uso total (m) | Desperdício (m)
     0 | [1, 0, 0]     |            80 |              70
     1 | [0, 1, 0]     |            60 |              90
     ...
```

### Lógica

```python
def print_patterns_table(patterns, item_sizes, bar_length):
    print(f"\n=== PADRÕES VIÁVEIS ENUMERADOS ===")
    print(f"Total: {len(patterns)} padrões\n")

    header = f"{'Índice':>6} | {'Padrão':<20} | {'Uso (m)':>8} | {'Desperdício (m)':>15}"
    print(header)
    print("-" * len(header))

    for idx, pat in enumerate(patterns):
        used = sum(pat[i] * item_sizes[i] for i in range(len(item_sizes)))
        waste = bar_length - used
        print(f"{idx:>6} | {str(pat):<20} | {used:>8} | {waste:>15}")
```

---

## Implementação — `main.py`

O `main()` orquestra todo o pipeline com tratamento de erros centralizado.

```python
def main() -> None:
    try:
        # 1. Entrada
        problem = get_problem_input()
        validate_input(problem)

        bar_length = problem["bar_length"]
        item_sizes = problem["item_sizes"]
        demands    = problem["demands"]

        # 2. Padrões
        patterns = generate_patterns(bar_length, item_sizes)
        print_patterns_table(patterns, item_sizes, bar_length)

        # 3. Modelo
        print_model_summary(patterns, item_sizes, demands, bar_length)

        # 4. Resolução
        solution = build_and_solve(patterns, bar_length, item_sizes, demands)

        # 5. Solução
        print_solution(solution, item_sizes, bar_length)

    except (ValueError, RuntimeError) as e:
        print(f"\nErro: {e}")
```

**Separadores visuais** entre seções melhoram a legibilidade:
```python
print("\n" + "=" * 55)
```

---

## Robustez

- Envolver o pipeline em `try/except (ValueError, RuntimeError)` — imprimir `f"Erro: {e}"` e sair limpo
- Se `status != "ÓTIMO"`, exibir bloco `[AVISO]` antes da tabela
- Não chamar `print_patterns_table` se o número de padrões for muito grande (>500) — imprimir apenas o total como aviso (opcional)
- Todos os rótulos, cabeçalhos e mensagens em português

---

## Interface com as outras tarefas

| De quem recebe | O que recebe |
|----------------|-------------|
| Tarefa 1       | `get_problem_input()`, `validate_input()`, `generate_patterns()`, `compute_waste()` |
| Tarefa 2       | `build_and_solve()`, `print_model_summary()` |

---

## Estratégia para trabalho paralelo

O Membro 3 pode desenvolver `output_formatter.py` e `main.py` **antes** das Tarefas 1 e 2
estarem prontas usando dados stub:

```python
# Dados de teste para print_solution
mock_solution = {
    "patterns":        [[1,1,0],[0,2,1]],
    "x_values":        [3, 50],
    "total_bars":      53,
    "total_waste":     1030.0,
    "status":          "ÓTIMO",
    "objective_value": 1030.0,
}
mock_item_sizes = [80, 60, 50]
mock_bar_length = 150

print_solution(mock_solution, mock_item_sizes, mock_bar_length)
```

Ao terminar as outras tarefas, basta trocar os dados stub pelos imports reais em `main.py`.

---

## Verificação

Após integrar todas as tarefas, executar com os dados do enunciado:

```
Comprimento da barra: 150
Quantidade de tipos:  3
Tamanhos: 80 60 50
Demandas: 70 100 120
```

Checar:
1. Saída exibe o modelo ILP com número correto de variáveis e restrições
2. Tabela de solução lista apenas padrões ativos (`x_j > 0`)
3. `Desperdício total = total_barras × 150 − (70×80 + 100×60 + 120×50)`
4. Testar entrada inválida (letra no lugar de número) → re-prompt, não crash
5. Testar entrada com item maior que a barra → mensagem de erro em português
