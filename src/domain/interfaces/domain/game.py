from typing import Protocol

from src.domain.dataclasses_.game_result import GameState
from src.domain.enums_.move_direction import MoveDirection


class IGame(Protocol):
    """
    Defines the core game interface for 2048.

    Any game implementation must provide these methods to handle game lifecycle and moves.
    """

    def start(self) -> GameState:
        """
        Initializes and starts a new game session.

        :return: Initial game state with starting tiles spawned
        """

    def make_move(self, direction: MoveDirection) -> GameState:
        """
        Processes player move in specified direction and updates game state.

        :param direction: Movement direction for tiles
        :return: Updated game state after move processing
        :raises: ValueError if move cannot be processed
        """
