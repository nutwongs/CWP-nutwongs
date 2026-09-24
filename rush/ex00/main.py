#!/usr/bin/env python3
"""Run checkmate() against sample boards."""
from checkmate import checkmate

def main():
    # Case 1: กรณีกรอก K สองตัว 
    print("Test 1: 2 K")
    board1 = """\
R...
..K.
..P.
.K.."""
    checkmate(board1)

    # Case 2: กรณี Success
    print("Test 2: K were exterminated.")
    board2 = """\
..K.
.P..
....
...."""
    checkmate(board2)

    # Case 3: กรณีไม่มี PBRQ มาจัดการ K
    print("Test 3: None PBRQ")
    board3 = """\
....
.K..
....
...."""
    checkmate(board3)

    # Case 4: กรณีไม่มี King เลย 
    print("Test 4: None K")
    board4 = """\
R...
....
..P.
...."""
    checkmate(board4)

    # Case 5: กระดานไม่ใช่สี่เหลี่ยม N*N
    print("Test 5: Chess board does not square")
    board5 = """\
R..
.K..
...."""
    checkmate(board5)


if __name__ == "__main__":
    main()