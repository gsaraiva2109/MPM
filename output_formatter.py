from __future__ import annotations

# Task 3 — Membro 3
# Formatação de saída e exibição dos resultados
# Ver docs/task3_plan.md para o plano completo de implementação.


def print_solution(solution: dict, item_sizes: list[int], bar_length: int) -> None:
    """
    Imprime a solução ótima em tabela formatada (em português).

    Exibe somente os padrões com x_values[j] > 0.

    Formato esperado:
        === SOLUÇÃO ÓTIMA ===
        Status: ÓTIMO

        Padrão           | Barras | Desperdício/barra
        [1, 1, 0]        |      3 |                10
        [0, 2, 1]        |     50 |                20
        ------------------------------------------------
        Total de barras utilizadas : 53
        Desperdício total          : 1030 m
        Valor objetivo             : 1030.0

    Args:
        solution:   dict retornado por build_and_solve()
        item_sizes: lista de tamanhos dos itens
        bar_length: comprimento da barra padrão
    """
    raise NotImplementedError("Tarefa 3: implementar print_solution()")


def print_patterns_table(
    patterns: list[list[int]], item_sizes: list[int], bar_length: int
) -> None:
    """
    Imprime todos os padrões enumerados com índice, vetor e desperdício.

    Útil para depuração e para o relatório acadêmico.

    Args:
        patterns:   lista completa de padrões viáveis
        item_sizes: lista de tamanhos dos itens
        bar_length: comprimento da barra padrão
    """
    raise NotImplementedError("Tarefa 3: implementar print_patterns_table()")
