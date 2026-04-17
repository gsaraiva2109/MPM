from __future__ import annotations


def get_problem_input() -> dict:
    """Prompt stdin interactively for all problem parameters with re-prompt on bad input."""
    print("=== PROBLEMA DE CORTE UNIDIMENSIONAL ===\n")

    bar_length = _read_positive_int("Comprimento da barra: ")

    n_types = _read_positive_int("Quantidade de tipos de itens: ")

    item_sizes: list[int] = []
    for i in range(n_types):
        while True:
            size = _read_positive_int(f"Tamanho do item {i + 1}: ")
            if size > bar_length:
                print(
                    f"Erro: o tamanho do item não pode ser maior que a barra ({bar_length})."
                )
                continue
            item_sizes.append(size)
            break

    demands: list[int] = []
    for i in range(n_types):
        demand = _read_positive_int(
            f"Demanda do item {i + 1} (tamanho {item_sizes[i]}): "
        )
        demands.append(demand)

    return {
        "bar_length": bar_length,
        "n_types": n_types,
        "item_sizes": item_sizes,
        "demands": demands,
    }


def validate_input(problem: dict) -> None:
    """Validate a problem dict. Raises ValueError with a descriptive message on any violation."""
    bar_length = problem["bar_length"]
    n_types = problem["n_types"]
    item_sizes = problem["item_sizes"]
    demands = problem["demands"]

    if bar_length < 1:
        raise ValueError("O comprimento da barra deve ser pelo menos 1.")
    if n_types < 1:
        raise ValueError("A quantidade de tipos deve ser pelo menos 1.")
    if len(item_sizes) != n_types:
        raise ValueError(
            f"Esperado {n_types} tamanho(s), mas recebeu {len(item_sizes)}."
        )
    if len(demands) != n_types:
        raise ValueError(
            f"Esperado {n_types} demanda(s), mas recebeu {len(demands)}."
        )
    for i, size in enumerate(item_sizes):
        if size < 1:
            raise ValueError(f"O tamanho do item {i + 1} deve ser pelo menos 1.")
        if size > bar_length:
            raise ValueError(
                f"O tamanho do item {i + 1} ({size}) não pode ser maior que a barra ({bar_length})."
            )
    for i, demand in enumerate(demands):
        if demand < 1:
            raise ValueError(f"A demanda do item {i + 1} deve ser pelo menos 1.")


# ── internal helper ──────────────────────────────────────────────────────────

def _read_positive_int(prompt: str) -> int:
    """Loop until the user enters a valid integer >= 1."""
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Erro: o valor deve ser pelo menos 1.")
                continue
            return value
        except ValueError:
            print("Erro: insira um número inteiro válido.")
