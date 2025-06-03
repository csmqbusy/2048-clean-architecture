import pytest

from src.domain.enums_.tile_value import TileValue
from src.domain.dataclasses_.tile_position import TilePosition
from src.domain.dataclasses_.tile import Tile
from src.domain.entities.game import Game
from src.domain.entities.tile_spawner import TileSpawner
from src.domain.entities.board import Board
from src.domain.dataclasses_.dimension import Dimension
from tests.unit.objects import board_with_full_column, empty_board


@pytest.fixture
def dimension() -> Dimension:
    yield Dimension(rows=4, cols=4)


@pytest.fixture
def board(dimension) -> Board:
    yield Board.create(dimension=dimension)


@pytest.fixture
def tile_spawner(dimension) -> TileSpawner:
    yield TileSpawner()


@pytest.fixture
def game(board, tile_spawner) -> Game:
    yield Game(
        board=board,
        tile_spawner=tile_spawner,
    )


@pytest.fixture
def tiles_for_board() -> list[list[Tile]]:
    yield board_with_full_column()


@pytest.fixture
def empty_tiles_for_board() -> list[list[Tile]]:
    yield empty_board()


@pytest.fixture
def board_with_tiles(tiles_for_board) -> Board:
    yield Board(tiles=tiles_for_board)


@pytest.fixture
def empty_tiles_positions(tiles_for_board) -> list[TilePosition]:
    yield [
        TilePosition(row_idx=row_idx, col_idx=col_idx)
        for row_idx, row in enumerate(tiles_for_board)
        for col_idx, tile in enumerate(row)
        if tile.value == TileValue.ZERO
    ]
