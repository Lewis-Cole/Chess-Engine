"""Handling user experience i.e. format of outputs and readability."""


from rules import piece_dictionary


def move_to_string(board, move):
    """Coverts a move on given board to readable string."""
    from_square = move[0]
    to_square = move[1]

    moving_piece = board[from_square[0]][from_square[1]]

    piece_string = piece_dictionary[moving_piece]

    move_string = "%s \t from %s to %s" % (piece_string, from_square, to_square)

    return move_string


def execute_move(board, move):
    """Executes a move on a board and gives new board as output."""
    from_square = move[0]
    to_square = move[1]

    moving_piece = board[from_square[0]][from_square[1]]

    board[to_square[0]][to_square[1]] = moving_piece

    board[from_square[0]][from_square[1]] = ""

    return board


def print_board(board):
    print("----------")
    for i in board:
        print(i)
    print("----------")
