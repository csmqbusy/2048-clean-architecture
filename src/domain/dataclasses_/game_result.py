from dataclasses import dataclass

from domain.dataclasses_.tile import Tile
from domain.enums_.game_result import GameResult
from domain.enums_.game_status import GameStatus
from domain.interfaces.domain.board import IBoard


# TODO: переместить и, возможно, использовать не только здесь
type Tiles = list[list[Tile]]


@dataclass
class GameState:
    """
    Represents the result of the game.
    """

    tiles: Tiles
    score: int
    status: GameStatus = GameStatus.IN_PROGRESS
    result: GameResult | None = None
