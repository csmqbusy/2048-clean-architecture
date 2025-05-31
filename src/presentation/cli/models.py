from dataclasses import dataclass
from enum import Enum


@dataclass
class CliRenderData:
    """Complete data required to render 2048 game in CLI"""
    tiles: list[list[str]]
    tiles_colors: list[list[str]]
    score: str
    message: str
    tile_width: int


class TileColor(Enum):
    """ANSI color codes for different tile values"""
    EMPTY = "\033[0m"
    TWO = "\033[1m\033[48;5;229m\033[38;5;94m"
    FOUR = "\033[1m\033[48;5;223m\033[38;5;94m"
    EIGHT = "\033[1m\033[48;5;216m\033[38;5;124m"
    SIXTEEN = "\033[1m\033[48;5;203m\033[38;5;124m"
    THIRTYTWO = "\033[1m\033[48;5;209m\033[38;5;124m"
    SIXTYFOUR = "\033[1m\033[48;5;208m\033[38;5;124m"
    ONETWOEIGHT = "\033[1m\033[48;5;227m\033[38;5;94m"
    TWOFIVESIX = "\033[1m\033[48;5;226m\033[38;5;94m"
    FIVEONETWO = "\033[1m\033[48;5;221m\033[38;5;94m"
    TENTWENTY4 = "\033[1m\033[48;5;220m\033[38;5;94m"
    TWENTY48 = "\033[1m\033[48;5;214m\033[38;5;94m"

    @classmethod
    def get_color(cls, value: int) -> str:
        """Get ANSI color code for tile value"""
        return {
            2: cls.TWO.value,
            4: cls.FOUR.value,
            8: cls.EIGHT.value,
            16: cls.SIXTEEN.value,
            32: cls.THIRTYTWO.value,
            64: cls.SIXTYFOUR.value,
            128: cls.ONETWOEIGHT.value,
            256: cls.TWOFIVESIX.value,
            512: cls.FIVEONETWO.value,
            1024: cls.TENTWENTY4.value,
            2048: cls.TWENTY48.value,
        }.get(value, cls.EMPTY.value)
