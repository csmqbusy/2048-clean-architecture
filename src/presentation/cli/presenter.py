from src.application.ports.presenter_output import IPresenterOutput
from src.domain.dataclasses_.game_result import GameState
from src.domain.enums_.game_result import GameResult
from src.domain.enums_.game_status import GameStatus
from src.domain.enums_.tile_value import TileValue
from src.presentation.cli.models import PresenterOutput


class CliPresenter:
    """Formats 2048 game data for CLI output."""

    _DEFAULT_IN_PROGRESS_MSG = "Merge the tiles and reach 2048! ✨"
    _DEFAULT_WIN_MSG = "Congratulations! You've won! 🎯 Want to try for a higher score?"
    _DEFAULT_LOSE_MSG = "Game over! Don't give up—try again and aim higher! 🔄"

    def __init__(
        self,
        in_progress_message: str = _DEFAULT_IN_PROGRESS_MSG,
        win_message: str = _DEFAULT_WIN_MSG,
        lose_message: str = _DEFAULT_LOSE_MSG,
    ):
        """
        Initializes the CLI presenter with display configuration.

        :param in_progress_message: Custom message to show during gameplay
        :param win_message: Custom message to show when player wins
        :param lose_message: Custom message to show when player loses
        """
        self._in_progress_message = in_progress_message
        self._win_message = win_message
        self._lose_message = lose_message

    def present(self, game_state: GameState) -> IPresenterOutput:
        """
        Converts game state to CLI-ready format.

        :param game_state: Current game state
        :return: Formatted tiles, score and message
        """
        formatted_board = []

        for row in game_state.tiles:
            formatted_row = [
                str(tile.value) if tile.value != TileValue.ZERO else "" for tile in row
            ]
            formatted_board.append(formatted_row)

        message = self._in_progress_message
        if game_state.status == GameStatus.COMPLETED:
            if game_state.result == GameResult.WIN:
                message = self._win_message
            elif game_state.result == GameResult.LOSE:
                message = self._lose_message

        score = f"Score: {game_state.score}"

        return PresenterOutput(
            tiles=formatted_board,
            score=score,
            message=message,
        )
