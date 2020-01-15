"""Testing file."""

from rules import starting_board
from legal_moves import find_moves
from interface import move_to_string, execute_move, print_board
from brain import play_game

play_game(starting_board, "w")






# x = find_moves(starting_board, "w")

# for i in x:
#     print(move_to_string(starting_board, i))

# print("-----")

# board_2 = execute_move(starting_board, x[2])

# print_board(board_2)

# board_1 = [
#     ["", "N", "B", "Q", "K", "B", "N", "R"],
#     ["", "P", "P", "P", "P", "P", "P", "P"],
#     ["", "", "", "", "", "", "", ""],
#     ["", "", "", "R", "", "", "", ""],
#     ["", "", "", "", "", "", "", ""],
#     ["", "", "", "", "", "", "", ""],
#     ["p", "p", "p", "p", "p", "p", "p", "p"],
#     ["r", "n", "b", "q", "k", "b", "n", "r"],
# ]

# y = find_moves(board_1, "w")

# for i in y:
#     print(i[1])
