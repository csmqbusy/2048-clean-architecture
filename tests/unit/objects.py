from src.domain.dataclasses_.tile import Tile
from src.domain.enums_.tile_value import TileValue


def empty_board() -> list[list[Tile]]:
    """Returns a completely empty game board with all tiles set to ZERO"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_with_win_condition() -> list[list[Tile]]:
    """Returns a board containing the winning tile (2048)"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.TEN), Tile(TileValue.TEN), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ELEVEN), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_with_lose_condition() -> list[list[Tile]]:
    """Returns a completely filled board with no possible moves (lose condition)"""
    return [
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)]
    ]


def board_with_one_possible_move() -> list[list[Tile]]:
    """Returns a completely filled board with no possible moves (lose condition)"""
    return [
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.THREE), Tile(TileValue.THREE)]
    ]


def board_with_full_column() -> list[list[Tile]]:
    """Returns a board with one completely filled column (no ZERO tiles)"""
    return [
        [Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_with_almost_win_condition() -> list[list[Tile]]:
    """Returns a board that's one move away from winning (contains 1024 tile)"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.TEN), Tile(TileValue.TEN)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_with_almost_win_condition_swipe_right() -> list[list[Tile]]:
    """Returns a board that's one move away from winning (contains 1024 tile)"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ELEVEN)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_random_state_1() -> list[list[Tile]]:
    """Returns a random board state where merges are possible in any direction"""
    return [
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.THREE), Tile(TileValue.THREE)],
        [Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ONE), Tile(TileValue.ZERO)],
        [Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.TWO), Tile(TileValue.TWO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ONE), Tile(TileValue.ZERO), Tile(TileValue.ONE)]
    ]


def board_random_state_1_swipe_left() -> list[list[Tile]]:
    """Returns the board after swiping left"""
    return [
        [Tile(TileValue.THREE), Tile(TileValue.FOUR), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_random_state_1_swipe_right() -> list[list[Tile]]:
    """Returns the board after CORRECTLY swiping right"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.THREE), Tile(TileValue.FOUR)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.TWO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.FOUR), Tile(TileValue.THREE)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.TWO)]
    ]


def board_random_state_1_swipe_up() -> list[list[Tile]]:
    """Returns the board after swiping up"""
    return [
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.THREE), Tile(TileValue.THREE)],
        [Tile(TileValue.ONE), Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_random_state_1_swipe_down() -> list[list[Tile]]:
    """Returns the board after swiping down"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.THREE), Tile(TileValue.THREE)],
        [Tile(TileValue.ONE), Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)]
    ]


def board_random_state_2() -> list[list[Tile]]:
    """Returns a random board state where merges are possible in any direction"""
    return [
        [Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.FOUR)],
        [Tile(TileValue.THREE), Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)]
    ]


def board_random_state_2_swipe_left() -> list[list[Tile]]:
    """Returns the board after swiping left"""
    return [
        [Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.ZERO)],
        [Tile(TileValue.THREE), Tile(TileValue.FIVE), Tile(TileValue.THREE), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)]
    ]


def board_random_state_2_swipe_right() -> list[list[Tile]]:
    """Returns the board after swiping right"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.FOUR)],
        [Tile(TileValue.ZERO), Tile(TileValue.THREE), Tile(TileValue.FIVE), Tile(TileValue.THREE)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)]
    ]


def board_random_state_2_swipe_up() -> list[list[Tile]]:
    """Returns the board after swiping up"""
    return [
        [Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.FOUR)],
        [Tile(TileValue.THREE), Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)]
    ]


def board_random_state_2_swipe_down() -> list[list[Tile]]:
    """Returns the board after swiping down"""
    return [
        [Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.FOUR)],
        [Tile(TileValue.THREE), Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE)],
        [Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)]
    ]


def board_random_state_3() -> list[list[Tile]]:
    """Returns a random board state where merges are possible in any direction"""
    return [
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.ONE)],
        [Tile(TileValue.ONE), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.TWO), Tile(TileValue.THREE)],
        [Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.THREE), Tile(TileValue.THREE)]
    ]


def board_random_state_3_swipe_left() -> list[list[Tile]]:
    """Returns the board after swiping left"""
    return [
        [Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.ZERO)],
        [Tile(TileValue.FOUR), Tile(TileValue.TWO), Tile(TileValue.THREE), Tile(TileValue.ZERO)],
        [Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.ZERO)]
    ]


def board_random_state_3_swipe_right() -> list[list[Tile]]:
    """Returns the board after swiping right"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ONE), Tile(TileValue.TWO), Tile(TileValue.TWO)],
        [Tile(TileValue.ZERO), Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.ONE)],
        [Tile(TileValue.ZERO), Tile(TileValue.FOUR), Tile(TileValue.TWO), Tile(TileValue.THREE)],
        [Tile(TileValue.ZERO), Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.FOUR)]
    ]


def board_random_state_3_swipe_up() -> list[list[Tile]]:
    """Returns the board after swiping up"""
    return [
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.TWO)],
        [Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.THREE), Tile(TileValue.FOUR)],
        [Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.ZERO)],
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)]
    ]


def board_random_state_3_swipe_down() -> list[list[Tile]]:
    """Returns the board after swiping down"""
    return [
        [Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO), Tile(TileValue.ZERO)],
        [Tile(TileValue.TWO), Tile(TileValue.TWO), Tile(TileValue.ONE), Tile(TileValue.ZERO)],
        [Tile(TileValue.THREE), Tile(TileValue.ONE), Tile(TileValue.THREE), Tile(TileValue.TWO)],
        [Tile(TileValue.FOUR), Tile(TileValue.FOUR), Tile(TileValue.THREE), Tile(TileValue.FOUR)]
    ]
