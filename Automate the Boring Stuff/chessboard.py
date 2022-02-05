# adjust as needed
valid_board = {
    "2a": "wpawn",
    "2b": "wpawn",
    "2c": "wpawn",
    "2d": "wpawn",
    "2e": "wpawn",
    "2f": "wpawn",
    "2g": "wpawn",
    "2h": "wpawn",
    "1a": "wrook",
    "1b": "wknight",
    "1c": "wbishop",
    "1d": "wking",
    "1e": "wqueen",
    "1f": "wbishop",
    "1g": "wknight",
    "1h": "wrook",
    "7a": "bpawn",
    "7b": "bpawn",
    "7c": "bpawn",
    "7d": "bpawn",
    "7e": "bpawn",
    "7f": "bpawn",
    "7g": "bpawn",
    "7h": "bpawn",
    "8a": "brook",
    "8b": "bknight",
    "8c": "bbishop",
    "8d": "bking",
    "8e": "bqueen",
    "8f": "bbishop",
    "8g": "bknight",
    "8h": "brook",
}

# change values as needed
test_board = {
    "2a": "wpawn",
    "2b": "wpawn",
    "2c": "wpawn",
    "2d": "wpawn",
    "2e": "wpawn",
    "2f": "wpawn",
    "2g": "wpawn",
    "2h": "wpawn",
    "1a": "wrook",
    "1b": "wknight",
    "1c": "wbishop",
    "1d": "wking",
    "1e": "wqueen",
    "1f": "wbishop",
    "1g": "wknight",
    "1h": "wrook",
    "7a": "bpawn",
    "7b": "bpawn",
    "7c": "bpawn",
    "7d": "bpawn",
    "7e": "bpawn",
    "7f": "bpawn",
    "7g": "bpawn",
    "7h": "bpawn",
    "8a": "brook",
    "8b": "bknight",
    "8c": "bbishop",
    "8d": "bking",
    "8e": "bqueen",
    "8f": "bbishop",
    "8g": "bknight",
    "8h": "brook",
}


def isValidChessBoard(valid, chessboard):
    """
    takes 2 dictionaries containing chess board pieces and placements
    1 valid board
    1 board to test
    returns whether or not the test board meets the valid board's conditions
    """
    valid_freq = {}
    valid_placement = {}
    for piece in valid:
        if valid[piece] not in valid_freq:
            valid_freq[valid[piece]] = 1
        else:
            valid_freq[valid[piece]] += 1

        # check placement
        if piece not in valid_placement:
            valid_placement[piece] = 1
        else:
            valid_placement[piece] += 1

    board_freq = {}
    board_placement = {}
    for piece in chessboard:
        if chessboard[piece] not in board_freq:
            board_freq[chessboard[piece]] = 1
        else:
            board_freq[chessboard[piece]] += 1

        # check placement
        if piece not in board_placement:
            board_placement[piece] = 1
        else:
            board_placement[piece] += 1

    if board_freq == valid_freq and valid_placement == board_placement:
        return print("This is a valid board")
    else:
        return print("This is not a valid board")


isValidChessBoard(valid_board, test_board)
