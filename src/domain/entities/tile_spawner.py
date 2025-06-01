import random

from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition
from domain.enums_.tile_value import TileValue


class TileSpawner:
    """Handles spawning new tiles on the game board with controlled probabilities."""

    def __init__(self, tile2_spawn_chance: int | None = None) -> None:
        """
        Initializes the tile spawner with a custom probability for TileValue.ONE.

        :param tile2_spawn_chance: Probability (0-1) of spawning TileValue.ONE
               instead of TileValue.TWO.
        """
        self._tile2_spawn_chance = tile2_spawn_chance or 0.9

    def spawn(self, board: list[list[Tile]], qty: int, empty_cells: list[TilePosition]) -> None:
        """
        Spawns new tiles on random empty positions of the board.

        :param board: 2D list representing the game board to modify.
        :param qty: Number of tiles to spawn (must be 1 or 2).
        :param empty_cells: Available positions for new tiles.
        :raises ValueError: If qty is not 1 or 2.
        """
        if qty not in (1, 2):
            raise ValueError("qty must be 1 or 2")

        unique_positions = set()
        while len(unique_positions) < qty:
            position = random.choice(empty_cells)
            unique_positions.add(position)

        for position in unique_positions:
            value = self._get_new_tile_value()
            board[position.row_idx][position.col_idx] = Tile(value=value)

    def _get_new_tile_value(self) -> TileValue:
        """
        Generates a new tile value based on configured probability.

        :return: TileValue.ONE (with spawn_chance probability) or TileValue.TWO.
        """
        return TileValue.ONE if random.random() < self._tile2_spawn_chance else TileValue.TWO
