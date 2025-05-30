from application.ports.presenter import IPresenter
from application.ports.presenter_output import IPresenterOutput
from application.ports.view import IView
from domain.dataclasses_.game_result import GameState
from domain.enums_.game_status import GameStatus
from domain.enums_.move_direction import MoveDirection
from domain.interfaces.domain.game import IGame


class GameLoopUseCase:
    def __init__(
        self,
        game: IGame,
        presenter: IPresenter,
        view: IView,
    ):
        self._game = game
        self._presenter = presenter
        self._view = view

    def execute(self):
        # init game
        init_state = self._game.start()

        init_view_data: IPresenterOutput = self._presenter.present(init_state)
        self._view.display(init_view_data)

        # game loop
        while True:
            move_direction: MoveDirection = self._view.get_next_move()

            state: GameState = self._game.make_move(move_direction)

            view_data: IPresenterOutput = self._presenter.present(state)
            self._view.display(view_data)

            if state.status is GameStatus.COMPLETED:
                break
