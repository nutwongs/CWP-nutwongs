#!/usr/bin/env python3
"""Detect whether the King standing on a square chessboard is in check."""

PIECES = "PBRQK"

# Steps radiating outwards from the King, as (row, col) offsets.
STRAIGHT = ((-1, 0), (1, 0), (0, -1), (0, 1))
DIAGONAL = ((-1, -1), (-1, 1), (1, -1), (1, 1))

# A Pawn captures diagonally upwards, so only the two squares just
# below the King can hold a Pawn that threatens it.
PAWN_SQUARES = ((1, -1), (1, 1))


def parse_board(board):
    """Return the board's rows, or None when the input is not a valid board."""
    if not isinstance(board, str):
        return None
    
  #  board = board.replace("\r\n", "\n").strip("\n")
    if not board:
        return None

    rows = board.split("\n")
    size = len(rows)
    for row in rows:
        if len(row) != size:
            return None
    return rows


def find_king(rows):
    """Return the King's (row, col), or None unless there is exactly one."""
    king = None
    for row_index, row in enumerate(rows):
        for col_index, square in enumerate(row):
            if square == "K":
                if king is not None:
                    return None  # มี King มากกว่า 1 ตัว
                king = (row_index, col_index)
    return king  # หากไม่เจอเลย จะ คืนค่า None (King 0 ตัว)


def threatens(piece, step, distance):
    """Say whether a piece reached by `step` at `distance` attacks the King."""
    if piece == "Q":
        return True
    if piece == "R":
        return step in STRAIGHT
    if piece == "B":
        return step in DIAGONAL
    if piece == "P":
        return distance == 1 and step in PAWN_SQUARES
    return False


def is_in_check(rows, king):
    """Walk outwards from the King along every line an enemy could arrive on."""
    size = len(rows)
    king_row, king_col = king
    for step in STRAIGHT + DIAGONAL:
        row_step, col_step = step
        row, col = king_row + row_step, king_col + col_step
        distance = 1
        while 0 <= row < size and 0 <= col < size:
            square = rows[row][col]
            if square in PIECES:
                if threatens(square, step, distance):
                    return True
                break  # ตัวหมากแรกที่เจอจะบล็อกการโจมตีของตัวด้านหลังทั้งหมด
            row += row_step
            col += col_step
            distance += 1
    return False


def checkmate(board):
    """Print Success when the King is in check, Fail when it is safe."""
    rows = parse_board(board)
    if rows is None:
        return  # Undefined behaviour: คืนการควบคุมโดยไม่พิมพ์อะไร
    king = find_king(rows)
    if king is None:
        return  # ไม่มี King หรือมีมากกว่า 1 ตัว
    print("Success" if is_in_check(rows, king) else "Fail")