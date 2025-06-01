import sys
import termios
import tty

from domain.enums_.move_direction import MoveDirection
from presentation.cli.models import CliRenderData


class CliView:
    """
    Command-line interface implementation for the 2048 game.
    Handles:
    - Rendering the game board with colored tiles and borders
    - Displaying game status and score
    - Capturing player input (arrow keys)
    - Managing terminal display settings
    """

    def __init__(
        self,
        default_color: str = "\033[0m",
        border_color: str = "\033[0;37m",
    ):
        self._default_color = default_color
        self._border_color = border_color

    def display(self, data: CliRenderData) -> None:
        """
        Renders the complete game interface including:
        - Game status message
        - Current score
        - Game board with colored tiles
        - Decorative borders

        :param data: Prepared render data containing tiles, colors, and game info
        """
        self._clear_screen()
        print(data.message, data.score, sep="\n")  # display game info

        dim = len(data.tiles)

        self._display_board_header(dim, data.tile_width)

        for row_i in range(dim):
            for component in self._get_tile_components(data.tile_width):
                self._display_separator()
                for tile, color in zip(data.tiles[row_i], data.tiles_colors[row_i]):
                    self._display_tile_component(tile, color, component, data.tile_width)
                self._display_separator()
                print()

            if row_i == dim - 1:
                self._display_board_footer(dim, data.tile_width)

    def get_next_move(self) -> MoveDirection:
        """
        Captures and returns the player's move direction from keyboard input.
        Continuously polls for input until a valid arrow key is pressed.
        Handles Ctrl+C interrupt for graceful exit.

        :return: Valid move direction from arrow key input
        """
        while True:
            try:
                key = self._get_key()
            except KeyboardInterrupt:
                print("Bye-bye!")
                sys.exit(0)

            if key == "\x1b[A":
                return MoveDirection.UP
            elif key == "\x1b[B":
                return MoveDirection.DOWN
            elif key == "\x1b[C":
                return MoveDirection.RIGHT
            elif key == "\x1b[D":
                return MoveDirection.LEFT

    def _get_key(self) -> str:
        """
        Reads a single key press from stdin in raw mode, handling escape sequences.
        Supports arrow keys (returns escape sequences) and interrupts on Ctrl+C.

        :return: String representing the pressed key or escape sequence
        :raises KeyboardInterrupt: When Ctrl+C is pressed
        """
        file_descriptor = sys.stdin.fileno()
        original_terminal_settings = termios.tcgetattr(file_descriptor)

        try:
            tty.setraw(sys.stdin.fileno())
            key_press = sys.stdin.read(1)

            if key_press == "\x03":  # Ctrl+C
                raise KeyboardInterrupt("Exit")

            if key_press == "\x1b":  # Escape sequence (arrow keys etc)
                key_press += sys.stdin.read(2)

            return key_press

        finally:
            # Restore original terminal settings
            termios.tcsetattr(
                file_descriptor, termios.TCSADRAIN, original_terminal_settings
            )

    def _get_tile_components(self, tile_width: int) -> tuple[str, ...]:
        """
        Generates the top, middle, and bottom components for tile rendering.

        :param tile_width: Width of each tile in characters
        :return: Tuple of three strings representing tile components
        """
        top = f"┌{'─' * tile_width}┐"
        mid = "│{}│"
        bot = f"└{'─' * tile_width}┘"

        return top, mid, bot

    def _clear_screen(self) -> None:
        """Clears the terminal screen and moves cursor to home position."""
        print("\033[H\033[J", end="")

    def _display_board_header(self, dim: int, tile_width: int) -> None:
        """
        Renders the top border of the game board.

        :param dim: Board dimension (number of tiles per side)
        :param tile_width: Width of each tile in characters
        """
        header = f"┌{'─' * dim * (tile_width + 2)}┐"
        print(self._apply_border_style(header))

    def _display_separator(self) -> None:
        """Prints a vertical separator with configured border color."""
        print(f"{self._border_color}│{self._default_color}", end="")

    def _display_tile_component(
        self,
        tile: str,
        color: str,
        component: str,
        tile_width: int,
    ) -> None:
        """
        Renders a single component of a tile with proper coloring.

        :param tile: Tile content to display
        :param color: ANSI color code for the tile
        :param component: Which tile component to render (top/mid/bottom)
        :param tile_width: Width of the tile in characters
        """
        if tile.strip().isdigit():
            print(f"{color}{component.format(tile)}{self._default_color}", end="")
        else:
            print(" " * (tile_width + 2), end="")

    def _display_board_footer(self, dim: int, tile_width: int) -> None:
        """
        Renders the bottom border of the game board.

        :param dim: Board dimension (number of tiles per side)
        :param tile_width: Width of each tile in characters
        """
        footer = f"└{'─' * dim * (tile_width + 2)}┘"
        print(self._apply_border_style(footer))

    def _apply_border_style(self, border: str) -> str:
        """
        Applies border styling to a string.

        :param border: The border string to style
        :return: Styled border string with color codes
        """
        return f"{self._border_color}{border}{self._default_color}"
