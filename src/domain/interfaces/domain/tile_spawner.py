from typing import Protocol

from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition


class ITileSpawner(Protocol):
    """
    Defines the interface for tile spawning functionality in the game.

    Any implementation must provide a way to spawn new tiles on the game board.
    """

    def spawn(self, board: list[list[Tile]], qty: int, empty_cells: list[TilePosition]) -> None:
        """
        Spawns new tiles on specified empty positions of the game board.

        :param board: 2D list representing the current game board state to be modified
        :param qty: Number of tiles to spawn (typically 1 or 2)
        :param empty_cells: List of available positions where new tiles can be placed
        :raises ValueError: If invalid quantity of tiles is requested
        """
