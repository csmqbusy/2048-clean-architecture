from application.ports.presenter import IPresenter
from application.ports.view import IView
from application.use_cases.game_use_case import GameLoopUseCase
from domain.dataclasses_.dimension import Dimension
from domain.entities.board import Board
from domain.entities.game import Game
from domain.entities.tile_spawner import TileSpawner
from domain.interfaces.domain.board import IBoard
from domain.interfaces.domain.game import IGame
from domain.interfaces.domain.tile_spawner import ITileSpawner
from presentation.cli.presenter import CliPresenter
from presentation.cli.view import CliView


def create_dimension_dependency() -> Dimension:
    return Dimension(rows=4, cols=4)


def create_board_dependency(dimension: Dimension) -> IBoard:
    return Board.create(dimension=dimension)


def create_tile_spawner_dependency(tile2_spawn_chance: int | None = None) -> ITileSpawner:
    return TileSpawner(tile2_spawn_chance=tile2_spawn_chance)


def create_game_dependency(board: IBoard, tile_spawner: ITileSpawner) -> IGame:
    return Game(
        board=board,
        tile_spawner=tile_spawner,
    )


def create_presenter_dependency() -> IPresenter:
    return CliPresenter()


def create_view_dependency() -> IView:
    return CliView()


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
