from __future__ import annotations

from typing import Protocol

from domain.dataclasses_.dimension import Dimension
from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition


class IBoard(Protocol):
    """
    Interface defining the contract for a game board in 2048.

    Any concrete implementation must provide these methods to interact with the board state.
    """

    def get_tiles(self) -> list[list[Tile]]:
        """
        Retrieves the current state of all tiles on the board.

        :return: 2D list of Tile objects representing the board's state.
        """

    def get_empty_tiles_positions(self) -> list[TilePosition]:
        """
        Finds all empty (TileValue.ZERO) positions on the board.

        :return: List of TilePosition objects marking empty cells.
        """

    @classmethod
    def create(cls, dimension: Dimension) -> IBoard:
        """
        Factory method to create a new empty board instance.

        :param dimension: Board dimensions (rows x columns).
        :return: New board instance initialized with empty tiles.
        """
