from typing import Protocol

from domain.dataclasses_.game_result import GameState
from domain.enums_.move_direction import MoveDirection


class IGame(Protocol):
    """
    Interface for class that represents a game.
    """

    def start(self) -> GameState:
        """

        :return:
        """

    def make_move(self, direction: MoveDirection) -> GameState:
        """
        Starts the game.

        :return: the result of the game
        """
