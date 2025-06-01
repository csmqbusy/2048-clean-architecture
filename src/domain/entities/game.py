import copy

from domain.dataclasses_.game_result import GameState
from domain.dataclasses_.tile import Tile
from domain.enums_.game_result import GameResult
from domain.enums_.game_status import GameStatus
from domain.enums_.move_direction import MoveDirection
from domain.enums_.tile_value import TileValue
from domain.interfaces.domain.board import IBoard
from domain.interfaces.domain.tile_spawner import ITileSpawner


class Game:
    """
    Represents the core game logic for 2048, handling moves, scoring and game state.

    Manages the game board, processes player moves, checks win/lose conditions,
    and spawns new tiles after valid moves.
    """

    def __init__(
        self,
        board: IBoard,
        tile_spawner: ITileSpawner,
    ) -> None:
        """
        Initializes a new game instance.

        :param board: The game board implementation
        :param tile_spawner: Tile spawner implementation
        """
        self._board = board
        self._dim = len(board.get_tiles())
        self._tile_spawner = tile_spawner
        self._score = 0

    def start(self) -> GameState:
        """
        Starts a new game by spawning initial tiles.

        :return: Initial game state with 2 spawned tiles
        """
        tiles: list[list[Tile]] = self._board.get_tiles()
        self._tile_spawner.spawn(tiles, 2, self._board.get_empty_tiles_positions())
        return GameState(
            tiles=self._board.get_tiles(),
            score=0,
            status=GameStatus.IN_PROGRESS,
            result=None,
        )

    def make_move(self, move_direction: MoveDirection) -> GameState:
        """
        Processes a player move and updates game state.

        :param move_direction: Direction to move tiles
        :return: Updated game state after move processing
        """
        tiles: list[list[Tile]] = self._board.get_tiles()
        tiles_before = copy.deepcopy(tiles)
        self._apply_move(move_direction, tiles)
        tiles_after = self._board.get_tiles()

        if self._has_board_changed(tiles_before, tiles_after):
            self._tile_spawner.spawn(
                tiles_after, 1, self._board.get_empty_tiles_positions()
            )

        game_result: GameResult | None = self._get_game_result(tiles_after)
        game_status = (
            GameStatus.IN_PROGRESS if game_result is None else GameStatus.COMPLETED
        )

        return GameState(
            tiles=tiles_after,
            score=self._score,
            status=game_status,
            result=game_result,
        )

    def _apply_move(self, move: MoveDirection, tiles: list[list[Tile]]) -> None:
        """
        Applies move in specified direction to the tiles.

        :param move: Direction to move
        :param tiles: Current board tiles to modify
        """
        if move == MoveDirection.UP:
            self._apply_move_up(tiles)
        elif move == MoveDirection.DOWN:
            self._apply_move_down(tiles)
        elif move == MoveDirection.RIGHT:
            self._apply_move_right(tiles)
        elif move == MoveDirection.LEFT:
            self._apply_move_left(tiles)

    def _apply_move_right(self, tiles: list[list[Tile]]) -> None:
        """
        Moves all tiles to the right, merging matching pairs.

        Example transformation:
        [0, 2, 2, 0]    =>   [0, 0, 0, 4]
        [0, 4, 4, 4]    =>   [0, 0, 4, 8]
        [2, 0, 2, 8]    =>   [0, 0, 4, 8]
        [4, 8, 16, 16]  =>   [0, 4, 8, 32]
        """
        # all zeros should "pop up" in the opposite for move direction
        for row in tiles:
            target = self._dim - 1
            source = self._dim - 2
            while source >= 0:
                if row[target].value != TileValue.ZERO:
                    source -= 1
                    target -= 1
                    continue

                if row[source].value != TileValue.ZERO:
                    row[source], row[target] = row[target], row[source]
                    source -= 1
                    target -= 1
                else:
                    source -= 1

        # merge tiles with the same value
        for row in tiles:
            target = self._dim - 1
            source = self._dim - 2
            while source >= 0:
                if row[target].value != TileValue.ZERO and row[target] == row[source]:
                    new_tile = Tile(value=row[target].value.next())
                    row[target] = new_tile
                    del row[source]
                    row.insert(0, Tile(value=TileValue.ZERO))
                    self._score += new_tile.value
                source -= 1
                target -= 1

    def _apply_move_left(self, tiles: list[list[Tile]]) -> None:
        """
        Moves all tiles to the left, merging matching pairs.

        Example transformation:
        [0, 2, 2, 0]    =>   [4, 0, 0, 0]
        [0, 4, 4, 4]    =>   [8, 4, 0, 0]
        [2, 0, 2, 8]    =>   [4, 8, 0, 0]
        [4, 8, 16, 16]  =>   [4, 8, 32, 0]
        """
        # all zeros should "pop up" in the opposite for move direction
        for row in tiles:
            target = 0
            source = 1
            while source < self._dim:
                if row[target].value != TileValue.ZERO:
                    source += 1
                    target += 1
                    continue

                if row[source].value != TileValue.ZERO:
                    row[source], row[target] = row[target], row[source]
                    source += 1
                    target += 1
                else:
                    source += 1

        # merge tiles with the same value
        for row in tiles:
            target = 0
            source = 1
            while source < self._dim:
                if row[target].value != TileValue.ZERO and row[target] == row[source]:
                    new_tile = Tile(value=row[target].value.next())
                    row[target] = new_tile
                    del row[source]
                    row.append(Tile(value=TileValue.ZERO))
                    self._score += new_tile.value
                source += 1
                target += 1

    def _apply_move_down(self, tiles: list[list[Tile]]) -> None:
        """
        Moves all tiles downward, merging matching pairs.

        Example transformation:
        [2, 0, 0, 0]   =>   [0, 0, 0, 0]
        [2, 4, 0, 0]   =>   [0, 0, 0, 0]
        [0, 4, 8, 0]   =>   [0, 8, 0, 0]
        [0, 8, 8, 16]  =>   [4, 8, 16, 16]
        """
        # all zeros should "pop up" in the opposite for move direction
        for i in range(self._dim):
            target = self._dim - 1
            source = self._dim - 2
            while source >= 0:
                if tiles[target][i].value != TileValue.ZERO:
                    source -= 1
                    target -= 1
                    continue

                if tiles[source][i].value != TileValue.ZERO:
                    tiles[source][i], tiles[target][i] = (
                        tiles[target][i],
                        tiles[source][i],
                    )
                    source -= 1
                    target -= 1
                else:
                    source -= 1

        # merge tiles with the same value
        for i in range(self._dim):
            target = self._dim - 1
            source = self._dim - 2
            while source >= 0:
                if (
                    tiles[target][i].value != TileValue.ZERO
                    and tiles[target][i] == tiles[source][i]
                ):
                    new_tile = Tile(value=tiles[target][i].value.next())
                    tiles[target][i] = new_tile

                    for j in range(source, 0, -1):
                        tiles[j][i] = tiles[j - 1][i]
                    tiles[0][i] = Tile(value=TileValue.ZERO)

                    self._score += new_tile.value

                source -= 1
                target -= 1

    def _apply_move_up(self, tiles: list[list[Tile]]) -> None:
        """
        Moves all tiles upward, merging matching pairs.

        Example transformation:
        [2, 0, 0, 0]   =>   [4, 8, 16, 16]
        [2, 4, 0, 0]   =>   [0, 8, 0, 0]
        [0, 4, 8, 0]   =>   [0, 0, 0, 0]
        [0, 8, 8, 16]  =>   [0, 0, 0, 0]
        """
        # all zeros should "pop up" in the opposite for move direction
        for i in range(self._dim):
            target = 0
            source = 1
            while source < self._dim:
                if tiles[target][i].value != TileValue.ZERO:
                    source += 1
                    target += 1
                    continue

                if tiles[source][i].value != TileValue.ZERO:
                    tiles[source][i], tiles[target][i] = (
                        tiles[target][i],
                        tiles[source][i],
                    )
                    source += 1
                    target += 1
                else:
                    source += 1

        # merge tiles with the same value
        for i in range(self._dim):
            target = 0
            source = 1
            while source < self._dim:
                if (
                    tiles[target][i].value != TileValue.ZERO
                    and tiles[target][i] == tiles[source][i]
                ):
                    new_tile = Tile(value=tiles[target][i].value.next())
                    tiles[target][i] = new_tile

                    for j in range(source, self._dim - 1):
                        tiles[j][i] = tiles[j + 1][i]
                    tiles[self._dim - 1][i] = Tile(value=TileValue.ZERO)

                    self._score += new_tile.value

                source += 1
                target += 1

    def _has_board_changed(
        self,
        tiles_before: list[list[Tile]],
        tiles_after: list[list[Tile]],
    ) -> bool:
        """
        Checks if board state changed after move attempt.

        :param tiles_before: Board state before move
        :param tiles_after: Board state after move
        :return: True if any tile changed position/value
        """
        for i in range(self._dim):
            for j in range(self._dim):
                if tiles_before[i][j].value != tiles_after[i][j].value:
                    return True
        return False

    def _get_game_result(self, tiles: list[list[Tile]]) -> GameResult | None:
        """
        Determines current game result (win/lose) based on board state.

        :param tiles: Current board tiles
        :return: GameResult if game ended, None otherwise
        """
        if self._is_win(tiles):
            return GameResult.WIN

        if self._is_lose(tiles):
            return GameResult.LOSE

        return None

    def _is_win(self, tiles: list[list[Tile]]) -> bool:
        """
        Checks if winning condition is met (TileValue.ELEVEN present).

        :param tiles: Current board tiles
        :return: True if winning tile found
        """
        for i in range(self._dim):
            for j in range(self._dim):
                if tiles[i][j].value == TileValue.ELEVEN:
                    return True
        return False

    def _is_lose(self, tiles: list[list[Tile]]) -> bool:
        """
        Checks if losing condition is met (no valid moves left).

        :param tiles: Current board tiles
        :return: True if no valid moves available
        """
        empty_tiles_positions = self._board.get_empty_tiles_positions()
        return len(empty_tiles_positions) == 0 and not self._has_moves_left(tiles)

    def _has_moves_left(self, tiles: list[list[Tile]]) -> bool:
        """
        Checks if any valid moves remain on the board.

        :param tiles: Current board tiles
        :return: True if at least one valid move exists
        """
        # search for available moves horizontally
        for row in tiles:
            for i in range(1, self._dim):
                if row[i - 1] == row[i]:
                    return True

        # search for available moves vertically
        for i in range(self._dim):
            for j in range(1, self._dim):
                if tiles[j - 1][i] == tiles[j][i]:
                    return True

        return False
