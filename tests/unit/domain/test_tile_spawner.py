import pytest

from src.domain.dataclasses_.tile import Tile
from src.domain.entities.game import Game
from src.domain.entities.tile_spawner import TileSpawner
from src.domain.enums_.tile_value import TileValue
from tests.unit.objects import board_random_state_1, empty_board


@pytest.mark.parametrize(
    "tiles, qty",
    [
        (empty_board(), 1),
        (empty_board(), 2),
        (board_random_state_1(), 1),
    ]
)
def test_spawn(game: Game, tile_spawner: TileSpawner, tiles: list[list[Tile]], qty: int):
    game._board._tiles = tiles
    empty_cells_before = game._board.get_empty_tiles_positions()

    tile_spawner.spawn(tiles, qty, empty_cells_before)

    empty_cells_after = game._board.get_empty_tiles_positions()
    assert empty_cells_after != empty_cells_before
    assert len(empty_cells_after) + qty == len(empty_cells_before)


def test__get_new_tile_value(tile_spawner):
    iterations = 1000
    tile2_chance = tile_spawner._tile2_spawn_chance
    min_expected_2 = (tile2_chance * iterations) - (iterations / 10)
    max_expected_4 = iterations - min_expected_2

    values: list[TileValue] = []
    for _ in range(iterations):
        values.append(tile_spawner._get_new_tile_value())

    assert values.count(TileValue.ONE) > min_expected_2
    assert values.count(TileValue.TWO) < max_expected_4
