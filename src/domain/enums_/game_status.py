from enum import Enum


class GameStatus(Enum):
    """
    Represents the current state of the game progress.
    """

    IN_PROGRESS = 0
    COMPLETED = 1
