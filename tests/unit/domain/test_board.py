from src.domain.entities.board import Board


def test_get_tiles(board_with_tiles, tiles_for_board):
    assert board_with_tiles.get_tiles() == tiles_for_board


def test_get_empty_tiles_positions(board_with_tiles, empty_tiles_positions):
    assert board_with_tiles.get_empty_tiles_positions() == empty_tiles_positions


def test_create(dimension, empty_tiles_for_board):
    assert Board.create(dimension=dimension).get_tiles() == empty_tiles_for_board
