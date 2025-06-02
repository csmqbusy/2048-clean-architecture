from dataclasses import dataclass

from src.domain.dataclasses_.tile import Tile
from src.domain.enums_.game_result import GameResult
from src.domain.enums_.game_status import GameStatus


@dataclass
class GameState:
    """
    Snapshot of the game state at a particular moment.

    Contains all necessary information to represent the current game status,
    including board configuration, player score, and game progress status.
    """

    tiles: list[list[Tile]]
    score: int
    status: GameStatus = GameStatus.IN_PROGRESS
    result: GameResult | None = None
