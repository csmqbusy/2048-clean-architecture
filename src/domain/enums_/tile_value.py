from __future__ import annotations

from enum import IntEnum


class TileValue(IntEnum):
    """
    Represents all possible tile values in the 2048 game with exponential progression.

    Enum names (ONE, TWO, etc.) correspond to powers of 2:
    - ONE = 2¹ (2)
    - TWO = 2² (4)
    - ...
    - ELEVEN = 2¹¹ (2048)

    The ZERO value represents an empty tile space on the board.
    """

    ZERO = 0
    ONE = 2
    TWO = 4
    THREE = 8
    FOUR = 16
    FIVE = 32
    SIX = 64
    SEVEN = 128
    EIGHT = 256
    NINE = 512
    TEN = 1024
    ELEVEN = 2048

    def next(self) -> TileValue:
        """
        Returns the next value in the progression sequence (current × 2).

        :return: Next TileValue in the sequence
        :raises StopIteration: When called on ELEVEN (maximum value)
        :example:
            >>> TileValue.ONE.next()
            <TileValue.TWO: 4>
        """
        members = list(self.__class__)
        index = members.index(self) + 1

        if index >= len(members):
            raise StopIteration("No more values")

        return members[index]
