from typing import Protocol

from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition


class ITileSpawner(Protocol):
    def spawn(self, board: list[list[Tile]], qty: int, empty_cells: list[TilePosition]) -> None:
        """
        Spawns a new tiles on a board.

        :param board:
        :param qty:
        :param empty_cells:
        :return:
        """
