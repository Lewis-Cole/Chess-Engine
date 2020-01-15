"""Brain of the engine for decision making."""


import random

from legal_moves import find_moves
from interface import move_to_string, execute_move, print_board


def play_game(board, colour_string):
    w_king_off = False
    b_king_off = False
    moves_taken = 0
    print("Starting game...")
    print_board(board)

    while not(w_king_off or b_king_off):
        print("----------")
        moves = find_moves(board, colour_string)
        num_moves = len(moves)
        rnd_num = random.randint(0, num_moves - 1)

        print(move_to_string(board, moves[rnd_num]))
        board = execute_move(board, moves[rnd_num])
        moves_taken += 1
        print_board(board)

        w_king_off = True
        b_king_off = True

        for row_index in range(8):
            for column_index in range(8):
                piece = board[row_index][column_index]
                if piece == "K":
                    w_king_off = False
                if piece == "k":
                    b_king_off = False

    print("----------")
    if w_king_off:
        winner = "Black"
    
    if b_king_off:
        winner = "White"
    
    print("%s won the game in %s moves." % (winner, moves_taken))
