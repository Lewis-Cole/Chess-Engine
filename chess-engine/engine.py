#engine here
board = { 
    "A1": "R","B1": "N","C1": "B","D1": "K","E1": "Q","F1": "B","G1": "N","H1": "R",
    "A2": "P","B2": "P","C2": "P","D2": "P","E2": "P","F2": "P","G2": "P","H2": "P",
    "A3": ".","B3": ".","C3": ".","D3": ".","E3": ".","F3": ".","G3": ".","H3": ".",
    "A4": ".","B4": ".","C4": ".","D4": ".","E4": ".","F4": ".","G4": ".","H4": ".",
    "A5": ".","B5": ".","C5": ".","D5": ".","E5": ".","F5": ".","G5": ".","H5": ".",
    "A6": ".","B6": ".","C6": ".","D6": ".","E6": ".","F6": ".","G6": ".","H6": ".",
    "A7": "p","B7": "p","C7": "p","D7": "p","E7": "p","F7": "p","G7": "p","H7": "p",
    "A8": "r","B8": "n","C8": "b","D8": "k","E8": "q","F8": "b","G8": "n","H8": "r",
}


alphabet = ["A","B","C","D","E","F","G","H"]

# takes string gives list
def moves(key):
    if board[key] =="p":   
        letter_index = alphabet.index(key[0])
        number_index = int(key[1])
        if number_index == 7:
            m = [key[0] + str(number_index-1), key[0] + str(number_index-2)]
        else:
            if number_index != 1:   
                m = [key[0] + str(number_index-1)]
            else:
                m=[]
        print m
        for x in m:
            if board[x] == "p" or board[x] == "r" or board[x] == "n" or board[x] == "b" or board[x] == "k" or board[x] == "q":
                m[m.index(x)]="."
                print "own piece check ran"
        return m
    pass


def move(a,b):  
    board[b]=board[a]
    board[a]="."


