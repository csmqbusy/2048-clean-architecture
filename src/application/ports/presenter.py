from typing import Protocol

from application.ports.presenter_output import IPresenterOutput
from domain.dataclasses_.game_result import GameState


class IPresenter(Protocol):
    def present(self, game_state: GameState) -> IPresenterOutput:
        """

        :return:
        """
