"""Find the legal moves for all pieces."""


from rules import white_pieces, black_pieces


# Functions for finding the legal move of each piece


def pawn_moves(board, colour_string, square_list):
    """Find all legal moves for a pawn."""
    # create empty string to append legal moves
    legal_moves = []

    # consider moves if pawn is white
    if colour_string == "w":
        # one square forward
        move_1 = [square_list[0] + 1, square_list[1]]
        if 0 <= move_1[0] <= 7:
            if board[move_1[0]][move_1[1]] == "":
                legal_moves.append(move_1)

                if square_list[0] == 1:
                    # two squares forward
                    move_2 = [square_list[0] + 2, square_list[1]]
                    if 0 <= move_2[0] <= 7:
                        if board[move_2[0]][move_2[1]] == "":
                            legal_moves.append(move_2)

            # diagonal captures
            move_3 = [square_list[0] + 1, square_list[1] + 1]
            if 0 <= move_3[1] <= 7:
                if board[move_3[0]][move_3[1]] in black_pieces:
                    legal_moves.append(move_3)

            move_4 = [square_list[0] + 1, square_list[1] - 1]
            if 0 <= move_4[1] <= 7:
                if board[move_4[0]][move_4[1]] in black_pieces:
                    legal_moves.append(move_4)

        return legal_moves

    # consider moves if pawn is black
    if colour_string == "b":
        # one square forward
        move_1 = [square_list[0] - 1, square_list[1]]
        if 0 <= move_1[0] <= 7:
            if board[move_1[0]][move_1[1]] == "":
                legal_moves.append(move_1)

                if square_list[0] == 6:
                    # two squares forward
                    move_2 = [square_list[0] - 2, square_list[1]]
                    if 0 <= move_2[0] <= 7:
                        if board[move_2[0]][move_2[1]] == "":
                            legal_moves.append(move_2)

            # diagonal captures
            move_3 = [square_list[0] - 1, square_list[1] + 1]
            if 0 <= move_3[1] <= 7:
                if board[move_3[0]][move_3[1]] in white_pieces:
                    legal_moves.append(move_3)

            move_4 = [square_list[0] - 1, square_list[1] - 1]
            if 0 <= move_4[1] <= 7:
                if board[move_4[0]][move_4[1]] in white_pieces:
                    legal_moves.append(move_4)

        return legal_moves


def rook_moves(board, colour_string, square_list):
    """Find all legal moves for a rook."""
    legal_moves = []

    # set the colour of opponents pieces
    if colour_string == "w":
        opponent_pieces = black_pieces

    if colour_string == "b":
        opponent_pieces = white_pieces

    # going up
    go_up = True
    up_index = 1
    while go_up:
        move = [square_list[0] + up_index, square_list[1]]
        up_index += 1
        if 0 <= move[0] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_up = False
            else:
                go_up = False
        else:
            go_up = False

    # going down
    go_down = True
    down_index = 1
    while go_down:
        move = [square_list[0] - down_index, square_list[1]]
        down_index += 1
        if 0 <= move[0] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_down = False
            else:
                go_down = False
        else:
            go_down = False

    # going right
    go_right = True
    right_index = 1
    while go_right:
        move = [square_list[0], square_list[1] + right_index]
        right_index += 1
        if 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_right = False
            else:
                go_right = False
        else:
            go_right = False

    # going left
    go_left = True
    left_index = 1
    while go_left:
        move = [square_list[0], square_list[1] - left_index]
        left_index += 1
        if 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_left = False
            else:
                go_left = False
        else:
            go_left = False

    return legal_moves


def knight_moves(board, colour_string, square_list):
    """Find all legal moves for a knight."""
    legal_moves = []

    # set the colour of opponents pieces
    if colour_string == "w":
        opponent_pieces = black_pieces

    if colour_string == "b":
        opponent_pieces = white_pieces

    move_1 = [square_list[0] - 2, square_list[1] + 1]
    if 0 <= move_1[0] <= 7 and 0 <= move_1[1] <= 7:
        if (
            board[move_1[0]][move_1[1]] == ""
            or board[move_1[0]][move_1[1]] in opponent_pieces
        ):
            legal_moves.append(move_1)

    move_2 = [square_list[0] - 1, square_list[1] + 2]
    if 0 <= move_2[0] <= 7 and 0 <= move_2[1] <= 7:
        if (
            board[move_2[0]][move_2[1]] == ""
            or board[move_2[0]][move_2[1]] in opponent_pieces
        ):
            legal_moves.append(move_2)

    move_3 = [square_list[0] + 1, square_list[1] + 2]
    if 0 <= move_3[0] <= 7 and 0 <= move_3[1] <= 7:
        if (
            board[move_3[0]][move_3[1]] == ""
            or board[move_3[0]][move_3[1]] in opponent_pieces
        ):
            legal_moves.append(move_3)

    move_4 = [square_list[0] + 2, square_list[1] + 1]
    if 0 <= move_4[0] <= 7 and 0 <= move_4[1] <= 7:
        if (
            board[move_4[0]][move_4[1]] == ""
            or board[move_4[0]][move_4[1]] in opponent_pieces
        ):
            legal_moves.append(move_4)

    move_5 = [square_list[0] + 2, square_list[1] - 1]
    if 0 <= move_5[0] <= 7 and 0 <= move_5[1] <= 7:
        if (
            board[move_5[0]][move_5[1]] == ""
            or board[move_5[0]][move_5[1]] in opponent_pieces
        ):
            legal_moves.append(move_5)

    move_6 = [square_list[0] + 1, square_list[1] - 2]
    if 0 <= move_6[0] <= 7 and 0 <= move_6[1] <= 7:
        if (
            board[move_6[0]][move_6[1]] == ""
            or board[move_6[0]][move_6[1]] in opponent_pieces
        ):
            legal_moves.append(move_6)

    move_7 = [square_list[0] - 1, square_list[1] - 2]
    if 0 <= move_7[0] <= 7 and 0 <= move_7[1] <= 7:
        if (
            board[move_7[0]][move_7[1]] == ""
            or board[move_7[0]][move_7[1]] in opponent_pieces
        ):
            legal_moves.append(move_7)

    move_8 = [square_list[0] - 2, square_list[1] - 1]
    if 0 <= move_8[0] <= 7 and 0 <= move_8[1] <= 7:
        if (
            board[move_8[0]][move_8[1]] == ""
            or board[move_8[0]][move_8[1]] in opponent_pieces
        ):
            legal_moves.append(move_8)

    return legal_moves


def bishop_moves(board, colour_string, square_list):
    """Find all legal moves for a bishop."""
    legal_moves = []

    if colour_string == "w":
        opponent_pieces = black_pieces

    if colour_string == "b":
        opponent_pieces = white_pieces

    # going up-right
    go_upright = True
    upright_index = 1
    while go_upright:
        move = [square_list[0] + upright_index, square_list[1] + upright_index]
        upright_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_upright = False
            else:
                go_upright = False
        else:
            go_upright = False

    # going down-right
    go_downright = True
    downright_index = 1
    while go_downright:
        move = [square_list[0] - downright_index, square_list[1] + downright_index]
        downright_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_downright = False
            else:
                go_downright = False
        else:
            go_downright = False

    # going down-left
    go_downleft = True
    downleft_index = 1
    while go_downleft:
        move = [square_list[0] - downleft_index, square_list[1] - downleft_index]
        downleft_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_downleft = False
            else:
                go_downleft = False
        else:
            go_downleft = False

    # going up-left
    go_upleft = True
    upleft_index = 1
    while go_upleft:
        move = [square_list[0] + upleft_index, square_list[1] - upleft_index]
        upleft_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_upleft = False
            else:
                go_upleft = False
        else:
            go_upleft = False

    return legal_moves


def queen_moves(board, colour_string, square_list):
    """Find all legal moves for a queen."""
    legal_moves = []

    if colour_string == "w":
        opponent_pieces = black_pieces

    if colour_string == "b":
        opponent_pieces = white_pieces

        # going up
    go_up = True
    up_index = 1
    while go_up:
        move = [square_list[0] + up_index, square_list[1]]
        up_index += 1
        if 0 <= move[0] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_up = False
            else:
                go_up = False
        else:
            go_up = False

    # going down
    go_down = True
    down_index = 1
    while go_down:
        move = [square_list[0] - down_index, square_list[1]]
        down_index += 1
        if 0 <= move[0] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_down = False
            else:
                go_down = False
        else:
            go_down = False

    # going right
    go_right = True
    right_index = 1
    while go_right:
        move = [square_list[0], square_list[1] + right_index]
        right_index += 1
        if 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_right = False
            else:
                go_right = False
        else:
            go_right = False

    # going left
    go_left = True
    left_index = 1
    while go_left:
        move = [square_list[0], square_list[1] - left_index]
        left_index += 1
        if 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_left = False
            else:
                go_left = False
        else:
            go_left = False

    # going up-right
    go_upright = True
    upright_index = 1
    while go_upright:
        move = [square_list[0] + upright_index, square_list[1] + upright_index]
        upright_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_upright = False
            else:
                go_upright = False
        else:
            go_upright = False

    # going down-right
    go_downright = True
    downright_index = 1
    while go_downright:
        move = [square_list[0] - downright_index, square_list[1] + downright_index]
        downright_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_downright = False
            else:
                go_downright = False
        else:
            go_downright = False

    # going down-left
    go_downleft = True
    downleft_index = 1
    while go_downleft:
        move = [square_list[0] - downleft_index, square_list[1] - downleft_index]
        downleft_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_downleft = False
            else:
                go_downleft = False
        else:
            go_downleft = False

    # going up-left
    go_upleft = True
    upleft_index = 1
    while go_upleft:
        move = [square_list[0] + upleft_index, square_list[1] - upleft_index]
        upleft_index += 1
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            if board[move[0]][move[1]] == "":
                legal_moves.append(move)
            elif board[move[0]][move[1]] in opponent_pieces:
                legal_moves.append(move)
                go_upleft = False
            else:
                go_upleft = False
        else:
            go_upleft = False

    return legal_moves


def king_moves(board, colour_string, square_list):
    """Find all legal moves for a king."""
    legal_moves = []

    if colour_string == "w":
        opponent_pieces = black_pieces

    if colour_string == "b":
        opponent_pieces = white_pieces

    move_1 = [square_list[0] + 1, square_list[1]]
    if 0 <= move_1[0] <= 7 and 0 <= move_1[1] <= 7:
        if (
            board[move_1[0]][move_1[1]] == ""
            or board[move_1[0]][move_1[1]] in opponent_pieces
        ):
            legal_moves.append(move_1)

    move_2 = [square_list[0] + 1, square_list[1] + 1]
    if 0 <= move_2[0] <= 7 and 0 <= move_2[1] <= 7:
        if (
            board[move_2[0]][move_2[1]] == ""
            or board[move_2[0]][move_2[1]] in opponent_pieces
        ):
            legal_moves.append(move_2)

    move_3 = [square_list[0], square_list[1] + 1]
    if 0 <= move_3[0] <= 7 and 0 <= move_3[1] <= 7:
        if (
            board[move_3[0]][move_3[1]] == ""
            or board[move_3[0]][move_3[1]] in opponent_pieces
        ):
            legal_moves.append(move_3)

    move_4 = [square_list[0] - 1, square_list[1] + 1]
    if 0 <= move_4[0] <= 7 and 0 <= move_4[1] <= 7:
        if (
            board[move_4[0]][move_4[1]] == ""
            or board[move_4[0]][move_4[1]] in opponent_pieces
        ):
            legal_moves.append(move_4)

    move_5 = [square_list[0] - 1, square_list[1]]
    if 0 <= move_5[0] <= 7 and 0 <= move_5[1] <= 7:
        if (
            board[move_5[0]][move_5[1]] == ""
            or board[move_5[0]][move_5[1]] in opponent_pieces
        ):
            legal_moves.append(move_5)

    move_6 = [square_list[0] - 1, square_list[1] - 1]
    if 0 <= move_6[0] <= 7 and 0 <= move_6[1] <= 7:
        if (
            board[move_6[0]][move_6[1]] == ""
            or board[move_6[0]][move_6[1]] in opponent_pieces
        ):
            legal_moves.append(move_6)

    move_7 = [square_list[0], square_list[1] - 1]
    if 0 <= move_7[0] <= 7 and 0 <= move_7[1] <= 7:
        if (
            board[move_7[0]][move_7[1]] == ""
            or board[move_7[0]][move_7[1]] in opponent_pieces
        ):
            legal_moves.append(move_7)

    move_8 = [square_list[0] + 1, square_list[1] - 1]
    if 0 <= move_8[0] <= 7 and 0 <= move_8[1] <= 7:
        if (
            board[move_8[0]][move_8[1]] == ""
            or board[move_8[0]][move_8[1]] in opponent_pieces
        ):
            legal_moves.append(move_8)

    return legal_moves


# Function for outputting all legal moves


def find_moves(board, colour_string):
    """Finds all the legal moves for a player"""
    legal_moves = []

    player_pieces = white_pieces if colour_string == "w" else black_pieces

    for row_index in range(8):
        for column_index in range(8):
            piece = board[row_index][column_index]
            if piece in player_pieces:
                if piece == "P" or piece == "p":
                    legal_moves.append(
                        [
                            "Pawn",
                            pawn_moves(board, colour_string, [row_index, column_index]),
                        ]
                    )
                if piece == "R" or piece == "r":
                    legal_moves.append(
                        [
                            "Rook",
                            rook_moves(board, colour_string, [row_index, column_index]),
                        ]
                    )
                if piece == "N" or piece == "n":
                    legal_moves.append(
                        [
                            "Knight",
                            knight_moves(
                                board, colour_string, [row_index, column_index]
                            ),
                        ]
                    )
                if piece == "B" or piece == "b":
                    legal_moves.append(
                        [
                            "Bishop",
                            bishop_moves(
                                board, colour_string, [row_index, column_index]
                            ),
                        ]
                    )
                if piece == "Q" or piece == "q":
                    legal_moves.append(
                        [
                            "Queen",
                            queen_moves(
                                board, colour_string, [row_index, column_index]
                            ),
                        ]
                    )
                if piece == "K" or piece == "k":
                    legal_moves.append(
                        [
                            "King",
                            king_moves(board, colour_string, [row_index, column_index]),
                        ]
                    )

    return legal_moves
