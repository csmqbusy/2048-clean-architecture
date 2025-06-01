from dataclasses import dataclass
from enum import Enum


@dataclass
class CliRenderData:
    """Container for all data required to render the 2048 game in a command-line interface."""
    tiles: list[list[str]]
    tiles_colors: list[list[str]]
    score: str
    message: str
    tile_width: int


class TileColor(Enum):
    """
    ANSI color escape codes for different 2048 tile values.
    Each value combines:
    - Text style (bold)
    - Background color
    - Foreground (text) color

    Colors use 256-color mode (xterm) for consistent terminal display.
    """
    EMPTY = "\033[0m"  # Reset to default
    TWO = "\033[1m\033[48;5;229m\033[38;5;94m"  # Light yellow / brown text
    FOUR = "\033[1m\033[48;5;223m\033[38;5;94m"  # Pale orange / brown text
    EIGHT = "\033[1m\033[48;5;216m\033[38;5;124m"  # Light coral / dark red text
    SIXTEEN = "\033[1m\033[48;5;203m\033[38;5;124m"  # Red / dark red text
    THIRTYTWO = "\033[1m\033[48;5;209m\033[38;5;124m"  # Orange-red / dark red text
    SIXTYFOUR = "\033[1m\033[48;5;208m\033[38;5;124m"  # Dark orange / dark red text
    ONETWOEIGHT = "\033[1m\033[48;5;227m\033[38;5;94m"  # Light yellow / brown text
    TWOFIVESIX = "\033[1m\033[48;5;226m\033[38;5;94m"  # Yellow / brown text
    FIVEONETWO = "\033[1m\033[48;5;221m\033[38;5;94m"  # Light goldenrod / brown text
    TENTWENTY4 = "\033[1m\033[48;5;220m\033[38;5;94m"  # Gold / brown text
    TWENTY48 = "\033[1m\033[48;5;214m\033[38;5;94m"  # Orange / brown text

    @classmethod
    def get_color(cls, value: int) -> str:
        """
        Gets ANSI color code for specific tile value.

        :param value: Numeric tile value (2, 4, 8, ..., 2048)
        :return: Corresponding ANSI color code string, default reset code if not found
        """
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
