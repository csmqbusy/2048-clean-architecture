from enum import Enum


class MoveDirection(Enum):
    """
    Represents valid movement directions for tiles on the game board.

    Used to control tile sliding and merging behavior in the 2048 game.
    """

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
