from application.ports.presenter import IPresenter
from application.ports.presenter_output import IPresenterOutput
from application.ports.view import IView
from domain.dataclasses_.game_result import GameState
from domain.enums_.game_status import GameStatus
from domain.enums_.move_direction import MoveDirection
from domain.interfaces.domain.game import IGame


class GameLoopUseCase:
    """
    Coordinates the main game loop for 2048, managing the interaction between:
    - Game logic (IGame)
    - Presentation layer (IPresenter)
    - User interface (IView)

    The loop continues until the game reaches a completed state (win/lose).
    """

    def __init__(
        self,
        game: IGame,
        presenter: IPresenter,
        view: IView,
    ):
        self._game = game
        self._presenter = presenter
        self._view = view

    def execute(self) -> None:
        """
        Runs the main game loop sequence:
        1. Initializes the game
        2. Displays initial state
        3. Processes player moves until game completion
        4. Updates and displays game state after each move

        The loop breaks when the game status becomes COMPLETED.
        """
        # Initialize game
        init_state = self._game.start()

        init_view_data: IPresenterOutput = self._presenter.present(init_state)
        self._view.display(init_view_data)

        # Main game loop
        while True:
            # Get player input
            move_direction: MoveDirection = self._view.get_next_move()

            # Process move and get new state
            state: GameState = self._game.make_move(move_direction)

            # Update display
            view_data: IPresenterOutput = self._presenter.present(state)
            self._view.display(view_data)

            # Check completion condition
            if state.status is GameStatus.COMPLETED:
                break
