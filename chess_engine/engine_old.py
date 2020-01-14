# engine here
board = {
    "A1": "R",
    "B1": "N",
    "C1": "B",
    "D1": "K",
    "E1": "Q",
    "F1": "B",
    "G1": "N",
    "H1": "R",
    "A2": "P",
    "B2": "P",
    "C2": "P",
    "D2": "P",
    "E2": "P",
    "F2": "P",
    "G2": "P",
    "H2": "P",
    "A3": ".",
    "B3": ".",
    "C3": ".",
    "D3": ".",
    "E3": ".",
    "F3": ".",
    "G3": ".",
    "H3": ".",
    "A4": ".",
    "B4": ".",
    "C4": ".",
    "D4": ".",
    "E4": ".",
    "F4": ".",
    "G4": ".",
    "H4": ".",
    "A5": ".",
    "B5": ".",
    "C5": ".",
    "D5": ".",
    "E5": ".",
    "F5": ".",
    "G5": ".",
    "H5": ".",
    "A6": ".",
    "B6": ".",
    "C6": ".",
    "D6": ".",
    "E6": ".",
    "F6": ".",
    "G6": ".",
    "H6": ".",
    "A7": "p",
    "B7": "p",
    "C7": "p",
    "D7": "p",
    "E7": "p",
    "F7": "p",
    "G7": "p",
    "H7": "p",
    "A8": "r",
    "B8": "n",
    "C8": "b",
    "D8": "k",
    "E8": "q",
    "F8": "b",
    "G8": "n",
    "H8": "r",
}

board_list = [
    "A1",
    "B1",
    "C1",
    "D1",
    "E1",
    "F1",
    "G1",
    "H1",
    "A2",
    "B2",
    "C2",
    "D2",
    "E2",
    "F2",
    "G2",
    "H2",
    "A3",
    "B3",
    "C3",
    "D3",
    "E3",
    "F3",
    "G3",
    "H3",
    "A4",
    "B4",
    "C4",
    "D4",
    "E4",
    "F4",
    "G4",
    "H4",
    "A5",
    "B5",
    "C5",
    "D5",
    "E5",
    "F5",
    "G5",
    "H5",
    "A6",
    "B6",
    "C6",
    "D6",
    "E6",
    "F6",
    "G6",
    "H6",
    "A7",
    "B7",
    "C7",
    "D7",
    "E7",
    "F7",
    "G7",
    "H7",
    "A8",
    "B8",
    "C8",
    "D8",
    "E8",
    "F8",
    "G8",
    "H8",
]

tot_moves = []
n_alphabet = [".", ".", "A", "B", "C", "D", "E", "F", "G", "H", ".", "."]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
# takes string gives list
def moves(key):
    letter_index = alphabet.index(key[0])
    n_letter_index = n_alphabet.index(key[0])
    number_index = int(key[1])

    if board[key] == "p":
        m = []
        a = key[0] + str(number_index - 1)
        if number_index == 7:
            b = key[0] + str(number_index - 2)
        else:
            b = "Q12"
        c = n_alphabet[n_letter_index - 1] + str(number_index - 1)
        d = n_alphabet[n_letter_index + 1] + str(number_index - 1)
        consider = [a, b, c, d]
        for x in range(0, 4):

            try:
                if (
                    board[consider[x]] == "P"
                    or board[consider[x]] == "R"
                    or board[consider[x]] == "B"
                    or board[consider[x]] == "N"
                    or board[consider[x]] == "Q"
                    or board[consider[x]] == "K"
                ) and (x == 2 or x == 3):
                    m.append(consider[x])

                else:
                    if (
                        board[consider[x]] == "p"
                        or board[consider[x]] == "r"
                        or board[consider[x]] == "b"
                        or board[consider[x]] == "n"
                        or board[consider[x]] == "q"
                        or board[consider[x]] == "k"
                        or board[consider[x]] == "P"
                        or board[consider[x]] == "R"
                        or board[consider[x]] == "B"
                        or board[consider[x]] == "N"
                        or board[consider[x]] == "Q"
                        or board[consider[x]] == "K"
                    ):
                        consider[1] = "Q12"
                        pass
                    # due to order of iteration, when space infront has our piece, this will force an exception when considering b. b may be set to Q12 when considering other places, to no consequence, as b is checked before c & d.
                    else:
                        if x == 2 or x == 3:
                            pass
                        else:
                            m.append(consider[x])
            except (KeyError):
                pass

        print("pawn")
        print(m)
        return m

    if board[key] == "r":
        # there's a quicker way to do this using one for loop that I might implement in the future
        m_north = []
        m_south = []
        m_east = []
        m_west = []
        # print("rook")
        for x in range((-1 * int(key[1])) + 1, 0):
            if (
                board[key[0] + str(-1 * x)] == "r"
                or board[key[0] + str(-1 * x)] == "n"
                or board[key[0] + str(-1 * x)] == "b"
                or board[key[0] + str(-1 * x)] == "k"
                or board[key[0] + str(-1 * x)] == "q"
                or board[key[0] + str(-1 * x)] == "p"
            ):
                break
            else:
                if (
                    board[key[0] + str(-1 * x)] == "R"
                    or board[key[0] + str(-1 * x)] == "N"
                    or board[key[0] + str(-1 * x)] == "B"
                    or board[key[0] + str(-1 * x)] == "K"
                    or board[key[0] + str(-1 * x)] == "Q"
                    or board[key[0] + str(-1 * x)] == "P"
                ):
                    m_north.append(key[0] + str(-1 * x))
                    break
                else:
                    m_north.append(key[0] + str(-1 * x))
        for x in range(int(key[1]) + 1, 9):
            if (
                board[key[0] + str(x)] == "r"
                or board[key[0] + str(x)] == "n"
                or board[key[0] + str(x)] == "b"
                or board[key[0] + str(x)] == "k"
                or board[key[0] + str(x)] == "q"
                or board[key[0] + str(x)] == "p"
            ):
                break
            else:
                if (
                    board[key[0] + str(x)] == "R"
                    or board[key[0] + str(x)] == "N"
                    or board[key[0] + str(x)] == "B"
                    or board[key[0] + str(x)] == "K"
                    or board[key[0] + str(x)] == "Q"
                    or board[key[0] + str(x)] == "P"
                ):
                    m_south.append(key[0] + str(x))
                    break
                else:
                    m_south.append(key[0] + str(x))

        for x in range(alphabet.index(key[0]) + 1, 8):
            if (
                board[alphabet[x] + key[1]] == "r"
                or board[alphabet[x] + key[1]] == "n"
                or board[alphabet[x] + key[1]] == "b"
                or board[alphabet[x] + key[1]] == "k"
                or board[alphabet[x] + key[1]] == "q"
                or board[alphabet[x] + key[1]] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[x] + key[1]] == "R"
                    or board[alphabet[x] + key[1]] == "N"
                    or board[alphabet[x] + key[1]] == "B"
                    or board[alphabet[x] + key[1]] == "K"
                    or board[alphabet[x] + key[1]] == "Q"
                    or board[alphabet[x] + key[1]] == "P"
                ):
                    m_east.append(alphabet[x] + key[1])
                    break
                else:
                    m_east.append(alphabet[x] + key[1])

        for x in range((-1 * alphabet.index(key[0])) + 1, 1):
            if (
                board[alphabet[-1 * x] + key[1]] == "r"
                or board[alphabet[-1 * x] + key[1]] == "n"
                or board[alphabet[-1 * x] + key[1]] == "b"
                or board[alphabet[-1 * x] + key[1]] == "k"
                or board[alphabet[-1 * x] + key[1]] == "q"
                or board[alphabet[-1 * x] + key[1]] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[-1 * x] + key[1]] == "R"
                    or board[alphabet[-1 * x] + key[1]] == "N"
                    or board[alphabet[-1 * x] + key[1]] == "B"
                    or board[alphabet[-1 * x] + key[1]] == "K"
                    or board[alphabet[-1 * x] + key[1]] == "Q"
                    or board[alphabet[-1 * x] + key[1]] == "P"
                ):
                    m_west.append(alphabet[-1 * x] + key[1])
                    break
                else:
                    m_west.append(alphabet[-1 * x] + key[1])
        m = []
        m.append([m_north, m_east, m_south, m_west])
        print("rook")
        print(m)
        return m

    if board[key] == "b":
        # print("bishop")
        # clockwise from upper right diagonal
        m = []
        m_NE = []
        m_SE = []
        m_SW = []
        m_NW = []
        n_dist = number_index - 1
        e_dist = 7 - letter_index
        s_dist = 8 - number_index
        w_dist = letter_index
        for x in range(1, min(n_dist, e_dist) + 1):
            if (
                board[alphabet[letter_index + x] + str(number_index - x)] == "r"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "n"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "b"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "k"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "q"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index + x] + str(number_index - x)] == "R"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "N"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "B"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "K"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "P"
                ):

                    m_NE.append(alphabet[letter_index + x] + str(number_index - x))
                    break
                else:
                    m_NE.append(alphabet[letter_index + x] + str(number_index - x))

        for x in range(1, min(s_dist, e_dist) + 1):
            if (
                board[alphabet[letter_index + x] + str(number_index + x)] == "r"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "n"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "b"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "k"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "q"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index + x] + str(number_index + x)] == "R"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "N"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "B"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "K"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "P"
                ):

                    m_SE.append(alphabet[letter_index + x] + str(number_index + x))
                    break

                else:
                    m_SE.append(alphabet[letter_index + x] + str(number_index + x))

        for x in range(1, min(s_dist, w_dist) + 1):
            if (
                board[alphabet[letter_index - x] + str(number_index + x)] == "r"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "n"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "b"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "k"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "q"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index - x] + str(number_index + x)] == "R"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "N"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "B"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "K"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "Q"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "P"
                ):

                    m_SW.append(alphabet[letter_index - x] + str(number_index + x))
                    break
                else:
                    m_SW.append(alphabet[letter_index - x] + str(number_index + x))

        for x in range(1, min(n_dist, w_dist) + 1):
            if (
                board[alphabet[letter_index - x] + str(number_index - x)] == "r"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "n"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "b"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "k"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "q"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index - x] + str(number_index - x)] == "R"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "N"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "B"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "K"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "P"
                ):

                    m_NW.append(alphabet[letter_index - x] + str(number_index - x))
                    break
                else:
                    m_NW.append(alphabet[letter_index - x] + str(number_index - x))

        m.append([m_NE, m_SE, m_SW, m_NW])
        print("bishop")
        print(m)
        return m

    if board[key] == "q":
        # print("queen")
        m = []
        m_north = []
        m_south = []
        m_east = []
        m_west = []
        m_NE = []
        m_SE = []
        m_SW = []
        m_NW = []
        n_dist = number_index - 1
        e_dist = 7 - letter_index
        s_dist = 8 - number_index
        w_dist = letter_index
        for x in range(1, min(n_dist, e_dist) + 1):
            if (
                board[alphabet[letter_index + x] + str(number_index - x)] == "r"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "n"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "b"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "k"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "q"
                or board[alphabet[letter_index + x] + str(number_index - x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index + x] + str(number_index - x)] == "R"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "N"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "B"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "K"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "P"
                ):

                    m_NE.append(alphabet[letter_index + x] + str(number_index - x))
                    break
                else:
                    m_NE.append(alphabet[letter_index + x] + str(number_index - x))

        for x in range(1, min(s_dist, e_dist) + 1):
            if (
                board[alphabet[letter_index + x] + str(number_index + x)] == "r"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "n"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "b"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "k"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "q"
                or board[alphabet[letter_index + x] + str(number_index + x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index + x] + str(number_index + x)] == "R"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "N"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "B"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "K"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index + x)] == "P"
                ):

                    m_SE.append(alphabet[letter_index + x] + str(number_index + x))
                    break

                else:
                    m_SE.append(alphabet[letter_index + x] + str(number_index + x))

        for x in range(1, min(s_dist, w_dist) + 1):
            if (
                board[alphabet[letter_index - x] + str(number_index + x)] == "r"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "n"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "b"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "k"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "q"
                or board[alphabet[letter_index - x] + str(number_index + x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index - x] + str(number_index + x)] == "R"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "N"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "B"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "K"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "Q"
                    or board[alphabet[letter_index - x] + str(number_index + x)] == "P"
                ):

                    m_SW.append(alphabet[letter_index - x] + str(number_index + x))
                    break
                else:
                    m_SW.append(alphabet[letter_index - x] + str(number_index + x))

        for x in range(1, min(n_dist, w_dist) + 1):
            if (
                board[alphabet[letter_index - x] + str(number_index - x)] == "r"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "n"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "b"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "k"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "q"
                or board[alphabet[letter_index - x] + str(number_index - x)] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[letter_index - x] + str(number_index - x)] == "R"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "N"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "B"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "K"
                    or board[alphabet[letter_index - x] + str(number_index - x)] == "Q"
                    or board[alphabet[letter_index + x] + str(number_index - x)] == "P"
                ):

                    m_NW.append(alphabet[letter_index - x] + str(number_index - x))
                    break
                else:
                    m_NW.append(alphabet[letter_index - x] + str(number_index - x))

        for x in range((-1 * int(key[1])) + 1, 0):
            if (
                board[key[0] + str(-1 * x)] == "r"
                or board[key[0] + str(-1 * x)] == "n"
                or board[key[0] + str(-1 * x)] == "b"
                or board[key[0] + str(-1 * x)] == "k"
                or board[key[0] + str(-1 * x)] == "q"
                or board[key[0] + str(-1 * x)] == "p"
            ):
                break
            else:
                if (
                    board[key[0] + str(-1 * x)] == "R"
                    or board[key[0] + str(-1 * x)] == "N"
                    or board[key[0] + str(-1 * x)] == "B"
                    or board[key[0] + str(-1 * x)] == "K"
                    or board[key[0] + str(-1 * x)] == "Q"
                    or board[key[0] + str(-1 * x)] == "P"
                ):
                    m_north.append(key[0] + str(-1 * x))
                    break
                else:
                    m_north.append(key[0] + str(-1 * x))
        for x in range(int(key[1]) + 1, 9):
            if (
                board[key[0] + str(x)] == "r"
                or board[key[0] + str(x)] == "n"
                or board[key[0] + str(x)] == "b"
                or board[key[0] + str(x)] == "k"
                or board[key[0] + str(x)] == "q"
                or board[key[0] + str(x)] == "p"
            ):
                break
            else:
                if (
                    board[key[0] + str(x)] == "R"
                    or board[key[0] + str(x)] == "N"
                    or board[key[0] + str(x)] == "B"
                    or board[key[0] + str(x)] == "K"
                    or board[key[0] + str(x)] == "Q"
                    or board[key[0] + str(x)] == "P"
                ):
                    m_south.append(key[0] + str(x))
                    break
                else:
                    m_south.append(key[0] + str(x))

        for x in range(alphabet.index(key[0]) + 1, 8):
            if (
                board[alphabet[x] + key[1]] == "r"
                or board[alphabet[x] + key[1]] == "n"
                or board[alphabet[x] + key[1]] == "b"
                or board[alphabet[x] + key[1]] == "k"
                or board[alphabet[x] + key[1]] == "q"
                or board[alphabet[x] + key[1]] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[x] + key[1]] == "R"
                    or board[alphabet[x] + key[1]] == "N"
                    or board[alphabet[x] + key[1]] == "B"
                    or board[alphabet[x] + key[1]] == "K"
                    or board[alphabet[x] + key[1]] == "Q"
                    or board[alphabet[x] + key[1]] == "P"
                ):
                    m_east.append(alphabet[x] + key[1])
                    break
                else:
                    m_east.append(alphabet[x] + key[1])

        for x in range((-1 * alphabet.index(key[0])) + 1, 1):
            if (
                board[alphabet[-1 * x] + key[1]] == "r"
                or board[alphabet[-1 * x] + key[1]] == "n"
                or board[alphabet[-1 * x] + key[1]] == "b"
                or board[alphabet[-1 * x] + key[1]] == "k"
                or board[alphabet[-1 * x] + key[1]] == "q"
                or board[alphabet[-1 * x] + key[1]] == "p"
            ):
                break
            else:
                if (
                    board[alphabet[-1 * x] + key[1]] == "R"
                    or board[alphabet[-1 * x] + key[1]] == "N"
                    or board[alphabet[-1 * x] + key[1]] == "B"
                    or board[alphabet[-1 * x] + key[1]] == "K"
                    or board[alphabet[-1 * x] + key[1]] == "Q"
                    or board[alphabet[-1 * x] + key[1]] == "P"
                ):
                    m_west.append(alphabet[-1 * x] + key[1])
                    break
                else:
                    m_west.append(alphabet[-1 * x] + key[1])
        m.append([m_north, m_east, m_south, m_west, m_NE, m_SE, m_SW, m_NW])
        print("queen")
        print(m)
        return m

    if board[key] == "n":
        # using new alphabet to avoid index error in alphabet function
        m = []
        a = n_alphabet[n_letter_index - 1] + str(number_index - 2)
        b = n_alphabet[n_letter_index + 1] + str(number_index - 2)
        c = n_alphabet[n_letter_index + 2] + str(number_index - 1)
        d = n_alphabet[n_letter_index + 2] + str(number_index + 1)
        e = n_alphabet[n_letter_index + 1] + str(number_index + 2)
        f = n_alphabet[n_letter_index - 1] + str(number_index + 2)
        g = n_alphabet[n_letter_index - 2] + str(number_index + 1)
        h = n_alphabet[n_letter_index - 2] + str(number_index - 1)
        consider = [a, b, c, d, e, f, g, h]
        for x in range(0, 8):
            try:
                if (
                    board[consider[x]] == "p"
                    or board[consider[x]] == "r"
                    or board[consider[x]] == "b"
                    or board[consider[x]] == "n"
                    or board[consider[x]] == "q"
                    or board[consider[x]] == "k"
                ):
                    pass
                else:
                    m.append(consider[x])
            except (KeyError):
                pass
        print("knight")
        print(m)
        return m

    if board[key] == "k":
        m = []
        n_letter_index = n_alphabet.index(key[0])
        a = n_alphabet[n_letter_index] + str(number_index - 1)
        b = n_alphabet[n_letter_index + 1] + str(number_index - 1)
        c = n_alphabet[n_letter_index + 1] + str(number_index)
        d = n_alphabet[n_letter_index + 1] + str(number_index + 1)
        e = n_alphabet[n_letter_index] + str(number_index + 1)
        f = n_alphabet[n_letter_index - 1] + str(number_index + 1)
        g = n_alphabet[n_letter_index - 1] + str(number_index)
        h = n_alphabet[n_letter_index - 1] + str(number_index - 1)
        consider = [a, b, c, d, e, f, g, h]
        for x in range(0, 8):
            try:
                if (
                    board[consider[x]] == "p"
                    or board[consider[x]] == "r"
                    or board[consider[x]] == "b"
                    or board[consider[x]] == "n"
                    or board[consider[x]] == "q"
                    or board[consider[x]] == "k"
                ):
                    pass
                else:
                    m.append(consider[x])
            except (KeyError):
                pass
        print("king")
        print(m)
        return m


def options():
    for x in range(0, 64):
        tot_moves.append(moves(board_list[x]))
    print(tot_moves)


def move(a, b):
    board[b] = board[a]
    board[a] = "."
