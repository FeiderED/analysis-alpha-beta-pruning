"""Implementación didáctica de minimax, negamax y poda alfa-beta.

Este archivo acompaña la guía LaTeX del repositorio. Está escrito para leerlo
paso a paso, no para maximizar rendimiento.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import inf
from typing import Callable, Iterable, Optional


@dataclass
class TreeNode:
    """Nodo simple para árboles de juego artificiales.

    Si ``value`` no es None, el nodo es terminal. Si tiene hijos, el valor se
    calcula recursivamente.
    """

    name: str
    value: Optional[int] = None
    children: Optional[list["TreeNode"]] = None

    def is_terminal(self) -> bool:
        return self.value is not None or not self.children


def minimax(node: TreeNode, maximizing: bool, counter: dict[str, int]) -> int:
    """Minimax clásico con dos tipos de niveles: MAX y MIN."""
    counter["visited"] += 1
    if node.is_terminal():
        assert node.value is not None
        return node.value

    assert node.children is not None
    if maximizing:
        best = -inf
        for child in node.children:
            best = max(best, minimax(child, False, counter))
        return int(best)

    best = inf
    for child in node.children:
        best = min(best, minimax(child, True, counter))
    return int(best)


def negamax(node: TreeNode, counter: dict[str, int]) -> int:
    """Negamax: una sola función porque el cambio de turno cambia el signo."""
    counter["visited"] += 1
    if node.is_terminal():
        assert node.value is not None
        return node.value

    assert node.children is not None
    return max(-negamax(child, counter) for child in node.children)


def alphabeta(
    node: TreeNode,
    alpha: float = -inf,
    beta: float = inf,
    counter: Optional[dict[str, int]] = None,
    trace: Optional[list[str]] = None,
    depth: int = 0,
) -> int:
    """Alfa-beta en forma negamax.

    Convención:
    - ``alpha`` es el mejor valor garantizado hasta ahora para quien mueve.
    - ``beta`` es el límite superior permitido por el rival.
    - Si alpha >= beta, el rival ya tiene una alternativa que evita este nodo,
      por lo que se poda el resto de hermanos.
    """
    if counter is None:
        counter = {"visited": 0, "cuts": 0}
    if trace is None:
        trace = []

    counter["visited"] += 1
    indent = "  " * depth
    trace.append(f"{indent}Visito {node.name}: ventana [{alpha}, {beta})")

    if node.is_terminal():
        assert node.value is not None
        trace.append(f"{indent}Terminal {node.name} = {node.value}")
        return node.value

    assert node.children is not None
    value = -inf
    for child in node.children:
        candidate = -alphabeta(child, -beta, -alpha, counter, trace, depth + 1)
        value = max(value, candidate)
        alpha = max(alpha, value)
        trace.append(
            f"{indent}Tras {child.name}: candidato={candidate}, mejor={value}, alpha={alpha}"
        )
        if alpha >= beta:
            counter["cuts"] += 1
            trace.append(f"{indent}PODA en {node.name}: alpha={alpha} >= beta={beta}")
            break
    return int(value)


# ---------------------------------------------------------------------------
# 3 en raya
# ---------------------------------------------------------------------------

Board = tuple[str, ...]  # nueve celdas: "X", "O" o "."
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def winner(board: Board) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != "." and board[a] == board[b] == board[c]:
            return board[a]
    if "." not in board:
        return "draw"
    return None


def legal_moves(board: Board) -> Iterable[int]:
    return (i for i, cell in enumerate(board) if cell == ".")


def play(board: Board, index: int, mark: str) -> Board:
    data = list(board)
    data[index] = mark
    return tuple(data)


def score_for_x(board: Board) -> int:
    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    return 0


def tictactoe_alphabeta(
    board: Board,
    turn: str,
    alpha: int = -2,
    beta: int = 2,
    counter: Optional[dict[str, int]] = None,
) -> int:
    """Alfa-beta para 3 en raya desde el punto de vista de X."""
    if counter is None:
        counter = {"visited": 0, "cuts": 0}
    counter["visited"] += 1

    result = winner(board)
    if result is not None:
        return score_for_x(board)

    if turn == "X":
        value = -2
        for move in legal_moves(board):
            value = max(value, tictactoe_alphabeta(play(board, move, "X"), "O", alpha, beta, counter))
            alpha = max(alpha, value)
            if alpha >= beta:
                counter["cuts"] += 1
                break
        return value

    value = 2
    for move in legal_moves(board):
        value = min(value, tictactoe_alphabeta(play(board, move, "O"), "X", alpha, beta, counter))
        beta = min(beta, value)
        if alpha >= beta:
            counter["cuts"] += 1
            break
    return value


def best_tictactoe_move(board: Board, turn: str = "X") -> tuple[int, int, dict[str, int]]:
    """Devuelve movimiento, valor y contadores para 3 en raya."""
    counter = {"visited": 0, "cuts": 0}
    best_move = -1
    best_value = -2 if turn == "X" else 2

    for move in legal_moves(board):
        child = play(board, move, turn)
        value = tictactoe_alphabeta(child, "O" if turn == "X" else "X", counter=counter)
        if turn == "X" and value > best_value:
            best_move, best_value = move, value
        if turn == "O" and value < best_value:
            best_move, best_value = move, value
    return best_move, best_value, counter


# ---------------------------------------------------------------------------
# Demostraciones rápidas
# ---------------------------------------------------------------------------


def sample_tree_ordered() -> TreeNode:
    """Árbol pequeño donde el orden ayuda a podar.

    La raíz está en convención minimax para la comparación clásica.
    """
    return TreeNode(
        "A",
        children=[
            TreeNode("B", children=[TreeNode("D", 3), TreeNode("E", 5)]),
            TreeNode("C", children=[TreeNode("F", 2), TreeNode("G", 9)]),
        ],
    )


def sample_tree_negamax() -> TreeNode:
    """Árbol en convención negamax con valores desde quien mueve en cada hoja."""
    return TreeNode(
        "p",
        children=[
            TreeNode("p1", children=[TreeNode("p11", -3), TreeNode("p12", -5)]),
            TreeNode("p2", children=[TreeNode("p21", -2), TreeNode("p22", -9)]),
        ],
    )


def format_board(board: Board) -> str:
    return "\n".join(" ".join(board[i:i + 3]) for i in range(0, 9, 3))


def main() -> None:
    tree = sample_tree_ordered()
    c1 = {"visited": 0}
    mm = minimax(tree, True, c1)
    print("Minimax clásico:", mm, c1)

    tree2 = sample_tree_negamax()
    c2 = {"visited": 0}
    nm = negamax(tree2, c2)
    print("Negamax:", nm, c2)

    c3 = {"visited": 0, "cuts": 0}
    trace: list[str] = []
    ab = alphabeta(tree2, counter=c3, trace=trace)
    print("Alfa-beta:", ab, c3)
    print("\nTraza alfa-beta:")
    print("\n".join(trace))

    board = (
        "X", "O", "X",
        ".", "O", ".",
        ".", ".", ".",
    )
    move, value, stats = best_tictactoe_move(board, "X")
    print("\n3 en raya:")
    print(format_board(board))
    print(f"Mejor movimiento para X: celda {move}, valor={value}, stats={stats}")


if __name__ == "__main__":
    main()
