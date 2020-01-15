"""Testing file."""


import numpy

from rules import starting_board
from legal_moves import find_moves
from interface import move_to_string, execute_move, print_board
from brain import play_game

board = starting_board
result = play_game(board, "w")

# moves_list = []

# for index in range(10):
#     board = starting_board
#     result = play_game(board, "w")
#     moves_list.append(result[1])

# avg_moves = numpy.mean(moves_list)

# print(avg_moves)


# x = find_moves(starting_board, "w")

# print(x)

# for i in x:
#     print(i)
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
