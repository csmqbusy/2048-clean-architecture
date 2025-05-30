from dataclasses import dataclass

from domain.dataclasses_.game_result import GameState

from enum import Enum

from domain.enums_.game_result import GameResult
from domain.enums_.game_status import GameStatus
from domain.enums_.tile_value import TileValue


class TileColor(Enum):
    EMPTY = "\033[0m"
    TWO = "\033[1m\033[48;5;229m\033[38;5;94m"
    FOUR = "\033[1m\033[48;5;223m\033[38;5;94m"
    EIGHT = "\033[1m\033[48;5;216m\033[38;5;124m"
    SIXTEEN = "\033[1m\033[48;5;203m\033[38;5;124m"
    THIRTYTWO = "\033[1m\033[48;5;209m\033[38;5;124m"
    SIXTYFOUR = "\033[1m\033[48;5;208m\033[38;5;124m"
    ONETWOEIGHT = "\033[1m\033[48;5;227m\033[38;5;94m"
    TWOFIVESIX = "\033[1m\033[48;5;226m\033[38;5;94m"
    FIVEONETWO = "\033[1m\033[48;5;221m\033[38;5;94m"
    TENTWENTY4 = "\033[1m\033[48;5;220m\033[38;5;94m"
    TWENTY48 = "\033[1m\033[48;5;214m\033[38;5;94m"

    @staticmethod
    def get_color(value: int) -> str:
        if value == 0:
            return TileColor.EMPTY.value
        if value == 2:
            return TileColor.TWO.value
        if value == 4:
            return TileColor.FOUR.value
        if value == 8:
            return TileColor.EIGHT.value
        if value == 16:
            return TileColor.SIXTEEN.value
        if value == 32:
            return TileColor.THIRTYTWO.value
        if value == 64:
            return TileColor.SIXTYFOUR.value
        if value == 128:
            return TileColor.ONETWOEIGHT.value
        if value == 256:
            return TileColor.TWOFIVESIX.value
        if value == 512:
            return TileColor.FIVEONETWO.value
        if value == 1024:
            return TileColor.TENTWENTY4.value
        if value == 2048:
            return TileColor.TWENTY48.value
        return TileColor.EMPTY.value


# TODO: переместить
@dataclass
class CliOutput:
    tiles: list[list[str]]
    tiles_colors: list[list[str]]
    score: str
    message: str
    tile_width: int


class CliPresenter:
    def __init__(self, tile_width: int = 6):
        self._tile_width = tile_width

    def present(self, game_state: GameState) -> CliOutput:
        """

        :return:
        """

        formatted_board = []
        tiles_colors = []

        for row in game_state.tiles:
            formatted_row = [f"{tile.value:^{self._tile_width}}" if tile.value != TileValue.ZERO else " " * self._tile_width for tile in row]
            formatted_board.append(formatted_row)
            row_colors = [TileColor.get_color(tile.value) for tile in row]
            tiles_colors.append(row_colors)

        message = "Merge the tiles and reach 2048! ✨"
        if game_state.status == GameStatus.COMPLETED:
            if game_state.result == GameResult.WIN:
                message = "Congratulations! You've won! 🎯 Want to try for a higher score?"
            elif game_state.result == GameResult.LOSE:
                message = "Game over! Don’t give up—try again and aim higher! 🔄"

        score = f"Score: {game_state.score}"

        return CliOutput(
            tiles=formatted_board,
            tiles_colors=tiles_colors,
            score=score,
            message=message,
            tile_width=self._tile_width,
        )
