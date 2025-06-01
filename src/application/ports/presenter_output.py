from typing import Protocol


class IPresenterOutput(Protocol):
    """
    Defines a standardized output format for presenting 2048 game data.
    This protocol ensures consistency in how game state is structured for different output methods
    (e.g., CLI, GUI, or API responses). All properties return strings for easy rendering.
    """

    @property
    def tiles(self) -> list[list[str]]: ...

    @property
    def score(self) -> str: ...

    @property
    def message(self) -> str: ...
