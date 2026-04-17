# Tarefa 2 — Modelo ILP e Resolução via OR-Tools

**Arquivo:** `ilp_model.py`  
**Dependência:** `pattern_generator.compute_waste` (Tarefa 1 — assinatura já definida)

---

## Objetivo

Construir e resolver o modelo de Programação Linear Inteira (PLI) do Problema de Corte
Unidimensional usando OR-Tools (`pywraplp`), e imprimir o modelo completo em português.

---

## Formulação Matemática

| Elemento     | Definição |
|--------------|-----------|
| Índices      | `j` = padrão de corte, `i` = tipo de item |
| Variáveis    | `x_j ∈ Z≥0` — quantidade de barras cortadas com o padrão `j` |
| Objetivo     | Minimizar `∑_j x_j · desperdício_j` onde `desperdício_j = bar_length − ∑_i padrão[j][i] · size_i` |
| Restrições   | Para cada tipo `i`: `∑_j padrão[j][i] · x_j ≥ demanda[i]` |

---

## Implementação — `build_and_solve()`

### 1. Criar o solver

```python
solver = pywraplp.Solver.CreateSolver('SCIP')
if solver is None:
    raise RuntimeError("Não foi possível criar o solver SCIP. Verifique a instalação do OR-Tools.")
```

### 2. Declarar variáveis

```python
x = [solver.IntVar(0, solver.infinity(), f'x_{j}') for j in range(len(patterns))]
```

### 3. Definir objetivo (minimizar desperdício total)

```python
objective = solver.Objective()
objective.SetMinimization()
for j, pat in enumerate(patterns):
    waste_j = compute_waste(pat, item_sizes, bar_length)
    objective.SetCoefficient(x[j], waste_j)
```

### 4. Adicionar restrições de demanda

```python
for i in range(len(demands)):
    ct = solver.Constraint(float(demands[i]), solver.infinity(), f'demanda_{i}')
    for j in range(len(patterns)):
        ct.SetCoefficient(x[j], patterns[j][i])
```

> **Atenção:** use `solver.Constraint(lb, ub, name)` + `SetCoefficient` — não use
> `solver.Add(expr >= valor)` com sum de list comprehension, pois pode causar
> comportamento inesperado no pywraplp.

### 5. Resolver e mapear status

```python
status_code = solver.Solve()
STATUS_MAP = {
    pywraplp.Solver.OPTIMAL:  "ÓTIMO",
    pywraplp.Solver.FEASIBLE: "VIÁVEL",
}
status = STATUS_MAP.get(status_code, "INVIÁVEL")
```

### 6. Ler solução e montar retorno

```python
if status in ("ÓTIMO", "VIÁVEL"):
    x_values = [int(round(x[j].solution_value())) for j in range(len(patterns))]
else:
    x_values = [0] * len(patterns)

total_bars  = sum(x_values)
total_waste = total_bars * bar_length - sum(demands[i] * item_sizes[i] for i in range(len(demands)))
assert total_waste >= 0, "Erro interno: desperdício total negativo."

return {
    "patterns":        patterns,
    "x_values":        x_values,
    "total_bars":      total_bars,
    "total_waste":     float(total_waste),
    "status":          status,
    "objective_value": solver.Objective().Value() if status != "INVIÁVEL" else 0.0,
}
```

---

## Implementação — `print_model_summary()`

Imprimir em português a formulação completa. Exemplo de saída esperada:

```
=== MODELO DE PROGRAMAÇÃO LINEAR INTEIRA ===
Variáveis: x_0, x_1, x_2, ..., x_{J-1}  (J padrões)

Objetivo: minimizar
  10*x_0 + 20*x_1 + 0*x_2 + ...

Restrições:
  demanda_0 (item 80m): 1*x_0 + 0*x_1 + ... >= 70
  demanda_1 (item 60m): 0*x_0 + 1*x_1 + ... >= 100
  demanda_2 (item 50m): 0*x_0 + 0*x_1 + ... >= 120
  x_j >= 0, inteiro  para todo j = 0..{J-1}
```

**Dicas de implementação:**
- Itere sobre `patterns` e `item_sizes` para construir cada linha
- Use `compute_waste(pat, item_sizes, bar_length)` para os coeficientes do objetivo
- Filtre termos com coeficiente zero para deixar a saída mais limpa (opcional)

---

## Robustez

- Verificar `solver is not None` imediatamente após `CreateSolver`
- Não chamar `solution_value()` se `status == "INVIÁVEL"`
- Usar `int(round(...))` nas variáveis para evitar artefatos de ponto flutuante
- Assegurar `total_waste >= 0` antes de retornar

---

## Interface com as outras tarefas

| De quem recebe | O que recebe |
|----------------|-------------|
| Tarefa 1       | `patterns: list[list[int]]`, `bar_length`, `item_sizes`, `demands` |

| Para quem entrega | O que entrega |
|-------------------|--------------|
| Tarefa 3           | dict `SolverSolution` (ver contratos de dados no plano geral) |
| Tarefa 3           | função `print_model_summary` (chamada por `main.py`) |

---

## Verificação

Após implementar, testar com os dados do enunciado:

```
bar_length = 150
item_sizes = [80, 60, 50]
demands    = [70, 100, 120]
```

Verificar:
- `status == "ÓTIMO"`
- `total_waste = total_bars × 150 − (70×80 + 100×60 + 120×50)`
- Para cada `i`: `sum(patterns[j][i] * x_values[j] for j) >= demands[i]`
- O modelo impresso tem exatamente `len(patterns)` variáveis e 3 restrições de demanda
