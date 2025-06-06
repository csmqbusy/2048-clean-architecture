from src.application.ports.presenter import IPresenter
from src.application.ports.view import IView
from src.application.use_cases.game_use_case import GameLoopUseCase
from src.domain.dataclasses_.dimension import Dimension
from src.domain.entities.board import Board
from src.domain.entities.game import Game
from src.domain.entities.tile_spawner import TileSpawner
from src.domain.interfaces.domain.board import IBoard
from src.domain.interfaces.domain.game import IGame
from src.domain.interfaces.domain.tile_spawner import ITileSpawner
from src.presentation.cli.presenter import CliPresenter
from src.presentation.cli.unix_view import UnixCliView


def create_dimension_dependency() -> Dimension:
    return Dimension(rows=4, cols=4)


def create_board_dependency(dimension: Dimension) -> IBoard:
    return Board.create(dimension=dimension)


def create_tile_spawner_dependency(
    tile2_spawn_chance: int | None = None,
) -> ITileSpawner:
    return TileSpawner(tile2_spawn_chance=tile2_spawn_chance)


def create_game_dependency(board: IBoard, tile_spawner: ITileSpawner) -> IGame:
    return Game(
        board=board,
        tile_spawner=tile_spawner,
    )


def create_presenter_dependency() -> IPresenter:
    return CliPresenter()


def create_view_dependency() -> IView:
    return UnixCliView()


def create_game_loop_dependency(
    game: IGame,
    presenter: IPresenter,
    view: IView,
) -> GameLoopUseCase:
    return GameLoopUseCase(
        game=game,
        presenter=presenter,
        view=view,
    )
