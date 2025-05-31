from dataclasses import dataclass

from domain.dataclasses_.tile import Tile
from domain.enums_.game_result import GameResult
from domain.enums_.game_status import GameStatus


@dataclass
class GameState:
    """
    Represents the result of the game.
    """

    tiles: list[list[Tile]]
    score: int
    status: GameStatus = GameStatus.IN_PROGRESS
    result: GameResult | None = None
