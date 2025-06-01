from dataclasses import dataclass


@dataclass
class TilePosition:
    """
    Represents a coordinate position of a tile on the game board.

    Stores row and column indices (0-based) and provides common position operations.
    This class is hashable and can be used as a dictionary key.
    """

    row_idx: int
    col_idx: int

    def __str__(self) -> str:
        return f"({self.row_idx}, {self.col_idx})"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.row_idx, self.col_idx))
