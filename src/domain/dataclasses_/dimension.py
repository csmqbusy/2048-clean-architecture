from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Dimension:
    """
    Represents the dimension of a board: number of rows and columns.
    """

    rows: int
    cols: int

    def __post_init__(self) -> None:
        # validate that the number of rows and columns is equal
        if self.rows != self.cols:
            raise ValueError("Number of rows and columns must be equal.")

        if self.rows < 4:
            raise ValueError("Dimension must be at least 4.")
