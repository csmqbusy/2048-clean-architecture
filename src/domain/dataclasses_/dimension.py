from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Dimension:
    """
    Represents the square dimensions of a game board (rows × columns).

    Provides validation to ensure the board remains square and meets minimum size requirements.
    Typical usage is for 4×4 boards in 2048 game.
    """

    rows: int
    cols: int

    def __post_init__(self) -> None:
        """
        Validates the dimension values after initialization.

        :raises ValueError: If either:
            - rows and cols are not equal (non-square board)
            - dimension is less than 4×4
        """
        if self.rows != self.cols:
            raise ValueError("Number of rows and columns must be equal.")

        if self.rows < 4:
            raise ValueError("Dimension must be at least 4.")
