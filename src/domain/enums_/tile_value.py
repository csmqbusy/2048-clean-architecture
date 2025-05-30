from enum import IntEnum


class TileValue(IntEnum):
    """
    Defines all possible tile values in 2048. Names (ONE, TWO...) represent
    progression levels where each level = previous × 2 (2¹, 2², 2³...).
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

    def next(self):
        members = list(self.__class__)
        index = members.index(self) + 1

        if index >= len(members):
            raise StopIteration("No more values")

        return members[index]
