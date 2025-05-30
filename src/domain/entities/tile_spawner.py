import random

from domain.dataclasses_.tile import Tile
from domain.dataclasses_.tile_position import TilePosition
from domain.enums_.tile_value import TileValue


class TileSpawner:
    def __init__(self, tile2_spawn_chance: int | None = None) -> None:
        self._tile2_spawn_chance = tile2_spawn_chance or 0.9

    def spawn(self, board: list[list[Tile]], qty: int, empty_cells: list[TilePosition]) -> None:
        """
        Spawns a new tiles on a board.

        :param board:
        :param qty:
        :param empty_cells:
        :return:
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
        return TileValue.ONE if random.random() < self._tile2_spawn_chance else TileValue.TWO
