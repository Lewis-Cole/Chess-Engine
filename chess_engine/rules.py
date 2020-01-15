"""The Rules and Setup for Chess."""

# Starting board for new game
starting_board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"],
]

# Group pieces by colour
white_pieces = ["P", "R", "N", "B", "Q", "K"]
black_pieces = ["p", "r", "n", "b", "q", "k"]

# Piece dictionary
piece_dictionary = {
    "P": "Pawn",
    "R": "Rook",
    "N": "Knight",
    "B": "Bishop",
    "Q": "Queen",
    "K": "King",
    "p": "Pawn",
    "r": "Rook",
    "n": "Knight",
    "b": "Bishop",
    "q": "Queen",
    "k": "King",
}
