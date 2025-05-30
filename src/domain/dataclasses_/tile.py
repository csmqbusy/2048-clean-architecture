from dataclasses import dataclass

from domain.enums_.tile_value import TileValue


@dataclass
class Tile:
    """
    Represents a tile on the board.
    """

    value: TileValue

    def __str__(self):
        return str(self.value)
