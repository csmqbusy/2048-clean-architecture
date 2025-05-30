from typing import Protocol


class IPresenterOutput(Protocol):
    @property
    def tiles(self) -> list[list[str]]: ...

    @property
    def score(self) -> str: ...

    @property
    def message(self) -> str: ...
