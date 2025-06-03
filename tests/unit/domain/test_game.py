import pytest

from src.domain.dataclasses_.game_result import GameState
from src.domain.dataclasses_.tile import Tile
from src.domain.entities.game import Game
from src.domain.enums_.game_result import GameResult
from src.domain.enums_.game_status import GameStatus
from src.domain.enums_.move_direction import MoveDirection
from tests.unit.objects import (
    board_random_state_1,
    board_random_state_1_swipe_down,
    board_random_state_1_swipe_left,
    board_random_state_1_swipe_right,
    board_random_state_1_swipe_up,
    board_random_state_2,
    board_random_state_2_swipe_down,
    board_random_state_2_swipe_left,
    board_random_state_2_swipe_right,
    board_random_state_2_swipe_up,
    board_random_state_3,
    board_random_state_3_swipe_down,
    board_random_state_3_swipe_left,
    board_random_state_3_swipe_right,
    board_random_state_3_swipe_up,
    board_with_almost_win_condition,
    board_with_almost_win_condition_swipe_right,
    board_with_lose_condition,
    board_with_one_possible_move,
    board_with_win_condition,
    empty_board,
)


def test_start(game: Game):
    game_state: GameState = game.start()
    assert game_state.tiles != empty_board
    assert game_state.score == 0
    assert game_state.status == GameStatus.IN_PROGRESS
    assert game_state.result is None


@pytest.mark.parametrize(
    (
            "tiles",
            "move",
            "expected_tiles",
            "spawned_tiles_qty",
            "score",
            "expected_score",
            "expected_status",
            "expected_result",
    ),
    [
        (
                board_with_lose_condition(),
                MoveDirection.RIGHT,
                board_with_lose_condition(),
                0,
                0,
                0,
                GameStatus.COMPLETED,
                GameResult.LOSE,
        ),
        (
                board_random_state_3(),
                MoveDirection.UP,
                board_random_state_3_swipe_up(),
                1,
                0,
                48,
                GameStatus.IN_PROGRESS,
                None,
        ),
        (
                board_with_almost_win_condition(),
                MoveDirection.RIGHT,
                board_with_almost_win_condition_swipe_right(),
                1,
                0,
                2048,
                GameStatus.COMPLETED,
                GameResult.WIN,
        ),
    ]
)
def test_make_move(
    game: Game,
    tiles: list[list[Tile]],
    move: MoveDirection,
    expected_tiles: list[list[Tile]],
    spawned_tiles_qty: int,
    score: int,
    expected_score: int,
    expected_status: GameStatus,
    expected_result: GameResult | None,
):
    game._board._tiles = tiles
    game_state: GameState = game.make_move(move_direction=move)

    differences = 0
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if game_state.tiles[i][j] != expected_tiles[i][j]:
                differences += 1

    # One new tile will be spawn after success move
    assert differences == spawned_tiles_qty

    assert game_state.score == expected_score
    assert game_state.status == expected_status
    assert game_state.result == expected_result


@pytest.mark.parametrize(
    "tiles, move, expected_result",
    [
        (board_with_lose_condition(), MoveDirection.RIGHT, board_with_lose_condition()),
        (board_random_state_1(), MoveDirection.RIGHT, board_random_state_1_swipe_right()),
        (board_random_state_2(), MoveDirection.LEFT, board_random_state_2_swipe_left()),
        (board_random_state_3(), MoveDirection.UP, board_random_state_3_swipe_up()),
    ]
)
def test__apply_move(
    game: Game,
    tiles: list[list[Tile]],
    move: MoveDirection,
    expected_result: list[list[Tile]],
):
    game._apply_move(move=move, tiles=tiles)
    assert tiles == expected_result


@pytest.mark.parametrize(
    "tiles, expected_result",
    [
        (board_with_lose_condition(), board_with_lose_condition()),
        (board_random_state_1(), board_random_state_1_swipe_right()),
        (board_random_state_2(), board_random_state_2_swipe_right()),
        (board_random_state_3(), board_random_state_3_swipe_right()),
    ]
)
def test__apply_move_right(
    game: Game, tiles: list[list[Tile]], expected_result: list[list[Tile]]
):
    game._apply_move_right(tiles)
    assert tiles == expected_result


@pytest.mark.parametrize(
    "tiles, expected_result",
    [
        (board_with_lose_condition(), board_with_lose_condition()),
        (board_random_state_1(), board_random_state_1_swipe_left()),
        (board_random_state_2(), board_random_state_2_swipe_left()),
        (board_random_state_3(), board_random_state_3_swipe_left()),
    ]
)
def test__apply_move_left(
    game: Game, tiles: list[list[Tile]], expected_result: list[list[Tile]]
):
    game._apply_move_left(tiles)
    assert tiles == expected_result


@pytest.mark.parametrize(
    "tiles, expected_result",
    [
        (board_with_lose_condition(), board_with_lose_condition()),
        (board_random_state_1(), board_random_state_1_swipe_down()),
        (board_random_state_2(), board_random_state_2_swipe_down()),
        (board_random_state_3(), board_random_state_3_swipe_down()),
    ]
)
def test__apply_move_down(
    game: Game, tiles: list[list[Tile]], expected_result: list[list[Tile]]
):
    game._apply_move_down(tiles)
    assert tiles == expected_result


@pytest.mark.parametrize(
    "tiles, expected_result",
    [
        (board_with_lose_condition(), board_with_lose_condition()),
        (board_random_state_1(), board_random_state_1_swipe_up()),
        (board_random_state_2(), board_random_state_2_swipe_up()),
        (board_random_state_3(), board_random_state_3_swipe_up()),
    ]
)
def test__apply_move_up(
    game: Game, tiles: list[list[Tile]], expected_result: list[list[Tile]]
):
    game._apply_move_up(tiles)
    assert tiles == expected_result


@pytest.mark.parametrize(
    "tiles_before, tiles_after, expected_result",
    [
        (board_random_state_1(), board_random_state_1(), False),
        (board_with_lose_condition(), board_with_lose_condition(), False),
        (empty_board(), empty_board(), False),
        (board_random_state_2(), board_random_state_2_swipe_up(), False),
        (board_random_state_3(), board_random_state_3_swipe_left(), True),
        (board_random_state_3(), board_random_state_3_swipe_up(), True),
    ]
)
def test__has_board_changed(
    game: Game,
    tiles_before: list[list[Tile]],
    tiles_after: list[list[Tile]],
    expected_result: bool,
):
    assert game._has_board_changed(tiles_before, tiles_after) == expected_result


@pytest.mark.parametrize(
    "tiles, expected_result",
    [
        (board_with_lose_condition(), GameResult.LOSE),
        (board_with_win_condition(), GameResult.WIN),
        (board_with_one_possible_move(), None),
        (board_random_state_1(), None),
    ]
)
def test__get_game_result(
    game: Game, tiles: list[list[Tile]], expected_result: GameResult | None
):
    game._board._tiles = tiles
    assert game._get_game_result(tiles) == expected_result
