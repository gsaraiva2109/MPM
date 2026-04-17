from __future__ import annotations

# Task 2 — Membro 2
# Modelo ILP e resolução via OR-Tools (pywraplp)
# Ver docs/task2_plan.md para o plano completo de implementação.

from ortools.linear_solver import pywraplp  # noqa: F401 (import verificado na implementação)
from pattern_generator import compute_waste  # noqa: F401


def build_and_solve(
    patterns: list[list[int]],
    bar_length: int,
    item_sizes: list[int],
    demands: list[int],
) -> dict:
    """
    Constrói e resolve o modelo ILP do Problema de Corte Unidimensional.

    Formulação:
        Variáveis : x_j ∈ Z≥0, uma por padrão j
        Objetivo  : minimizar sum_j(x_j * desperdício_j)
        Restrições: para cada tipo i, sum_j(padrão[j][i] * x_j) >= demanda[i]

    Args:
        patterns:   lista de padrões viáveis (de generate_patterns)
        bar_length: comprimento da barra padrão
        item_sizes: tamanho de cada tipo de item
        demands:    demanda de cada tipo de item

    Returns:
        dict com chaves:
            "patterns"        : list[list[int]]
            "x_values"        : list[int]   — barras cortadas por padrão
            "total_bars"      : int
            "total_waste"     : float
            "status"          : str  — "ÓTIMO" | "VIÁVEL" | "INVIÁVEL"
            "objective_value" : float
    """
    raise NotImplementedError("Tarefa 2: implementar build_and_solve()")


def print_model_summary(
    patterns: list[list[int]],
    item_sizes: list[int],
    demands: list[int],
    bar_length: int,
) -> None:
    """
    Imprime o modelo ILP completo (variáveis, objetivo, restrições) em português.

    Formato esperado:
        === MODELO DE PROGRAMAÇÃO LINEAR INTEIRA ===
        Variáveis: x_0, x_1, ..., x_{J-1}
        Objetivo: minimizar  w_0*x_0 + w_1*x_1 + ...
        Restrições:
          demanda_0: a_{0,0}*x_0 + a_{1,0}*x_1 + ... >= demands[0]
          ...
          x_j >= 0, inteiro  para todo j
    """
    raise NotImplementedError("Tarefa 2: implementar print_model_summary()")
