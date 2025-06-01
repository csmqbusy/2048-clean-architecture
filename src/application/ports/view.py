from typing import Protocol

from application.ports.presenter_output import IPresenterOutput
from domain.enums_.move_direction import MoveDirection


class IView(Protocol):
    """
    Interface for user interaction in the 2048 game.
    Defines methods for displaying game state and receiving player input.
    Implementations can vary for different interfaces (CLI, GUI, etc.).
    """

    def display(self, data: IPresenterOutput) -> None:
        """
        Renders the current game state to the user.

        :param data: Structured game data ready for display, containing tiles, score, and message.
        :return: None
        """

    def get_next_move(self) -> MoveDirection:
        """
        Captures and returns the player's next move direction.
        Should handle input validation internally (retry on invalid input).

        :return: Valid move direction chosen by the player.
        """
