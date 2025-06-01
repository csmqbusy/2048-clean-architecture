from enum import Enum


class GameResult(Enum):
    """
    Represents the possible final outcomes of a 2048 game session.
    """

    WIN = 0
    LOSE = 1
