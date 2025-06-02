from dataclasses import dataclass

from src.domain.enums_.tile_value import TileValue


@dataclass
class Tile:
    """
    Represents a single tile on the 2048 game board.

    Each tile carries a value that determines its visual representation
    and merge behavior in the game. The value comes from TileValue enum.
    """

    value: TileValue

    def __str__(self):
        return str(self.value)
