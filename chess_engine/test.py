"""Testing file."""

from rules import starting_board
from legal_moves import find_moves

x = find_moves(starting_board, "w")

for i in x:
    print(i)

print("-----")

board_1 = [
    ["", "N", "B", "Q", "K", "B", "N", "R"],
    ["", "P", "P", "P", "P", "P", "P", "P"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "R", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"],
]

y = find_moves(board_1, "w")

for i in y:
    print(i)
