from typing import Protocol

from application.ports.presenter_output import IPresenterOutput
from domain.enums_.move_direction import MoveDirection


class IView(Protocol):
    def display(self, data: IPresenterOutput) -> None:
        """

        :return:
        """

    def get_next_move(self) -> MoveDirection:
        """

        :return:
        """
