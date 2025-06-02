from typing import Protocol

from src.application.ports.presenter_output import IPresenterOutput
from src.domain.dataclasses_.game_result import GameState


class IPresenter(Protocol):
    """
    Defines an interface for presenting game state data in a format suitable for the output layer.
    Implementations should transform raw game state into a structured output (e.g., CLI, GUI, API response).
    """

    def present(self, game_state: GameState) -> IPresenterOutput:
        """
        Transforms the current game state into a standardized output format.

        :param game_state: Contains all relevant game data (board, score, status, etc.) to be presented.
        :return: Formatted output adhering to the IPresenterOutput protocol (e.g., serializable data for views).
        """
