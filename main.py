from __future__ import annotations

# Ponto de entrada — Tarefa 3 (Membro 3)
# Ver docs/task3_plan.md para o plano completo de implementação.

from input_handler import get_problem_input, validate_input
from pattern_generator import generate_patterns
from ilp_model import build_and_solve, print_model_summary
from output_formatter import print_solution, print_patterns_table


def main() -> None:
    """
    Orquestra o pipeline completo:

    1. Leitura e validação da entrada (Tarefa 1)
    2. Geração dos padrões de corte (Tarefa 1)
    3. Exibição do modelo ILP (Tarefa 2)
    4. Resolução do modelo (Tarefa 2)
    5. Exibição da solução (Tarefa 3)
    """
    raise NotImplementedError("Tarefa 3: implementar main()")


if __name__ == "__main__":
    main()
