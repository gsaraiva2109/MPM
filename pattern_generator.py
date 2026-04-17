from __future__ import annotations


def generate_patterns(bar_length: int, item_sizes: list[int]) -> list[list[int]]:
    results: list[list[int]] = []
    current = [0] * len(item_sizes)
    _enumerate(0, bar_length, current, results, item_sizes)
    if not results:
        raise RuntimeError("Nenhum padrão viável encontrado.")
    return results


def compute_waste(pattern: list[int], item_sizes: list[int], bar_length: int) -> int:
    """Return the trim loss (waste) of a single cutting pattern."""
    used = sum(pattern[i] * item_sizes[i] for i in range(len(item_sizes)))
    waste = bar_length - used
    assert waste >= 0, (
        f"Erro interno: desperdício negativo ({waste}) para o padrão {pattern}."
    )
    return waste


# ── internal recursion ───────────────────────────────────────────────────────

def _enumerate(
    idx: int,
    remaining: int,
    current: list[int],
    results: list[list[int]],
    item_sizes: list[int],
) -> None:
    if idx == len(item_sizes):
        if any(c > 0 for c in current):
            results.append(current[:])
        return
    max_qty = remaining // item_sizes[idx]
    for qty in range(0, max_qty + 1):
        current[idx] = qty
        _enumerate(idx + 1, remaining - qty * item_sizes[idx], current, results, item_sizes)
    current[idx] = 0
