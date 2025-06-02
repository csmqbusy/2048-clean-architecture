from __future__ import annotations

from src.domain.dataclasses_.dimension import Dimension
from src.domain.dataclasses_.tile import Tile
from src.domain.dataclasses_.tile_position import TilePosition
from src.domain.enums_.tile_value import TileValue


class Board:
    """Represents the game board in 2048, containing tiles and their positions."""

    def __init__(self, tiles: list[list[Tile]]) -> None:
        self._tiles = tiles

    def get_tiles(self) -> list[list[Tile]]:
        """
        Returns a list of all tiles on the board at the current moment.

        :return: a list of all tiles.
        """
        return self._tiles

    def get_empty_tiles_positions(self) -> list[TilePosition]:
        """
        Returns a list of positions of all empty tiles on the board at the
        current moment.

        :return: a list of positions of all empty tiles on the board.
        """
        return [
            TilePosition(row_idx=row_idx, col_idx=col_idx)
            for row_idx, row in enumerate(self._tiles)
            for col_idx, tile in enumerate(row)
            if tile.value == TileValue.ZERO
        ]

    @classmethod
    def create(cls, dimension: Dimension) -> Board:
        """
        Creates a new empty board with the specified dimensions.

        :param dimension: The size of the board (rows x cols).
        :return: A new Board instance filled with empty tiles (TileValue.ZERO).
        """
        default_value: TileValue = TileValue.ZERO

        tiles: list[list[Tile]] = [
            [Tile(value=default_value) for _ in range(dimension.cols)]
            for _ in range(dimension.rows)
        ]

        return cls(tiles=tiles)
