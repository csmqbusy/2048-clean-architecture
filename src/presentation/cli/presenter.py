from domain.dataclasses_.game_result import GameState
from domain.enums_.game_result import GameResult
from domain.enums_.game_status import GameStatus
from domain.enums_.tile_value import TileValue
from presentation.cli.models import CliRenderData, TileColor


class CliPresenter:
    """Present 2048 game state in command line interface"""

    _DEFAULT_IN_PROGRESS_MSG = "Merge the tiles and reach 2048! ✨"
    _DEFAULT_WIN_MSG = "Congratulations! You've won! 🎯 Want to try for a higher score?"
    _DEFAULT_LOSE_MSG = "Game over! Don’t give up—try again and aim higher! 🔄"

    def __init__(
        self,
        tile_width: int = 6,
        in_progress_message: str = _DEFAULT_IN_PROGRESS_MSG,
        win_message: str = _DEFAULT_WIN_MSG,
        lose_message: str = _DEFAULT_LOSE_MSG,
    ):
        if tile_width < 4:
            raise ValueError("Tile width must be at least 4")

        self._tile_width = tile_width
        self._in_progress_message = in_progress_message
        self._win_message = win_message
        self._lose_message = lose_message

    def present(self, game_state: GameState) -> CliRenderData:
        """

        :return:
        """

        formatted_board = []
        tiles_colors = []

        for row in game_state.tiles:
            formatted_row = [
                f"{tile.value:^{self._tile_width}}"
                if tile.value != TileValue.ZERO else " " * self._tile_width
                for tile in row
            ]
            formatted_board.append(formatted_row)
            row_colors = [TileColor.get_color(tile.value) for tile in row]
            tiles_colors.append(row_colors)

        message = self._in_progress_message
        if game_state.status == GameStatus.COMPLETED:
            if game_state.result == GameResult.WIN:
                message = self._win_message
            elif game_state.result == GameResult.LOSE:
                message = self._lose_message

        score = f"Score: {game_state.score}"

        return CliRenderData(
            tiles=formatted_board,
            tiles_colors=tiles_colors,
            score=score,
            message=message,
            tile_width=self._tile_width,
        )
