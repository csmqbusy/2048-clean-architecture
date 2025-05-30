from enum import Enum

from domain.dataclasses_.dimension import Dimension


class SupportedDimensions(Enum):
    """
    Represents supported dimensions for a board. Board must be a square
    with a side of at least 4 cells.
    """

    FOUR_ON_FOUR = Dimension(rows=4, cols=4)
