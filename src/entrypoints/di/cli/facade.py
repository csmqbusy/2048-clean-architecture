from dataclasses import dataclass

from application.ports.logger import ILogger
from application.use_cases.game_use_case import GameLoopUseCase
from domain.interfaces.domain.game import IGame
from entrypoints.di.cli.container import (
    create_dimension_dependency,
    create_board_dependency,
    create_tile_spawner_dependency,
    create_game_dependency,
    create_presenter_dependency,
    create_view_dependency,
    create_game_loop_dependency,
)


@dataclass
class Dependencies:
    game_loop: GameLoopUseCase


def dependencies_facade() -> Dependencies:
    dimension = create_dimension_dependency()

    board = create_board_dependency(dimension=dimension)

    tile_spawner = create_tile_spawner_dependency()

    game = create_game_dependency(board=board, tile_spawner=tile_spawner)

    presenter = create_presenter_dependency()

    view = create_view_dependency()

    game_loop = create_game_loop_dependency(game=game, presenter=presenter, view=view)

    return Dependencies(game_loop=game_loop)
