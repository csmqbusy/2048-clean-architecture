from __future__ import annotations

from typing import Protocol

from domain.dataclasses_.dimension import Dimension
from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition


class IBoard(Protocol):
    """
    Interface for class that represents a board in the game.
    """

    def get_tiles(self) -> list[list[Tile]]:
        """
        Returns a list of all tiles on the board at the current moment.

        :return: a list of all tiles.
        """

    def get_empty_tiles_positions(self) -> list[TilePosition]:
        """
        Returns a list of positions of all empty tiles on the board at the
        current moment.

        :return: a list of positions of all empty tiles.
        """

    @classmethod
    def create(cls, dim: Dimension) -> IBoard:
        """
        Factory method to create a board of a given dimension.

        :param dim: dimension of the board.
        :return: a new board with the given dimension.
        """
