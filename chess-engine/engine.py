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
numbers = ["1","2","3","4","5","6","7","8"]
# takes string gives list
def moves(key):
    letter_index = alphabet.index(key[0])
    number_index = int(key[1])
    print key
    print board[key]
    if board[key] =="p":
        print "pawn"   
        if number_index == 7:
            m = [key[0] + str(number_index-1), key[0] + str(number_index-2)]
        else:
            if number_index != 1:   
                m = [key[0] + str(number_index-1)]
            else:
                m=[]
        print m
        if board[m[0]] == "r" or board[m[0]] == "n" or board[m[0]] == "b" or board[m[0]] == "k" or board[m[0]] == "q" or board[m[0]] == "p":
            m=[]
            print "own piece check ran"
        return m
    else:
        pass
    
    
    if board[key] == "r":
        #there's a quicker way to do this using one for loop that I will implement in the future
        m_north = []
        m_south = []
        m_east = []
        m_west = []
        print "rook"
        for x in range((-1*int(key[1]))+1,0):
            if board[key[0]+str(-1*x)] == "r" or board[key[0]+str(-1*x)] == "n" or board[key[0]+str(-1*x)] == "b" or board[key[0]+str(-1*x)] == "k" or board[key[0]+str(-1*x)] == "q" or board[key[0]+str(-1*x)] == "p":
                break
            else:
                m_north.append(key[0]+str(-1*x))
        for x in range(int(key[1])+1,9):
            if board[key[0]+str(x)] == "r" or board[key[0]+str(x)] == "n" or board[key[0]+str(x)] == "b" or board[key[0]+str(x)] == "k" or board[key[0]+str(x)] == "q" or board[key[0]+str(x)] == "p":    
                break
            else:
                m_south.append(key[0]+str(x))
        for x in range(alphabet.index(key[0])+1,8):
            if board[alphabet[x]+key[1]] == "r" or board[alphabet[x]+key[1]] == "n" or board[alphabet[x]+key[1]] == "b" or board[alphabet[x]+key[1]] == "k" or board[alphabet[x]+key[1]] == "q" or board[alphabet[x]+key[1]] == "p":
                break
            else:
                m_east.append(alphabet[x]+key[1])
        for x in range((-1*alphabet.index(key[0]))+1,1):
            if board[alphabet[-1*x]+key[1]] == "r" or board[alphabet[-1*x]+key[1]] == "n" or board[alphabet[-1*x]+key[1]] == "b" or board[alphabet[-1*x]+key[1]] == "k" or board[alphabet[-1*x]+key[1]] == "q" or board[alphabet[-1*x]+key[1]] == "p":    
                break
            else:
                m_west.append(alphabet[-1*x]+key[1])
        m=[]
        m.append([m_north,m_east,m_south,m_west])
        return m
    
    
    if board[key] == "b":
        print "bishop"
        #clockwise from upper right diagonal 
        m = []
        m_NE = []
        m_SE = []
        m_SW = []
        m_NW = []
        n_dist = number_index-1
        e_dist = 7-letter_index
        s_dist = 8-number_index
        w_dist = letter_index 
        for x in range(1, min(n_dist,e_dist)+1):
            if board[alphabet[letter_index + x]+str(number_index - x)] == "r" or board[alphabet[letter_index + x]+str(number_index - x)] == "n" or board[alphabet[letter_index + x]+str(number_index - x)] == "b" or board[alphabet[letter_index + x]+str(number_index - x)] == "k" or board[alphabet[letter_index + x]+str(number_index - x)] == "q" or board[alphabet[letter_index + x]+str(number_index - x)] == "p":          
                break
            else:
                m_NE.append(alphabet[letter_index + x] + str(number_index - x))
        for x in range(1, min(s_dist,e_dist)+1):
            if board[alphabet[letter_index + x]+str(number_index + x)] == "r" or board[alphabet[letter_index + x]+str(number_index + x)] == "n" or board[alphabet[letter_index + x]+str(number_index + x)] == "b" or board[alphabet[letter_index + x]+str(number_index + x)] == "k" or board[alphabet[letter_index + x]+str(number_index + x)] == "q" or board[alphabet[letter_index + x]+str(number_index + x)] == "p":
                break
            else:
                m_SE.append(alphabet[letter_index + x] + str(number_index + x))
        for x in range(1, min(s_dist,w_dist)+1):
            if board[alphabet[letter_index - x]+str(number_index + x)] == "r" or board[alphabet[letter_index - x]+str(number_index + x)] == "n" or board[alphabet[letter_index - x]+str(number_index + x)] == "b" or board[alphabet[letter_index - x]+str(number_index + x)] == "k" or board[alphabet[letter_index - x]+str(number_index + x)] == "q" or board[alphabet[letter_index - x]+str(number_index + x)] == "p":
                break
            else:
                m_SW.append(alphabet[letter_index - x] + str(number_index + x))
        for x in range(1, min(n_dist,w_dist)+1):
            if board[alphabet[letter_index - x]+str(number_index - x)] == "r" or board[alphabet[letter_index - x]+str(number_index - x)] == "n" or board[alphabet[letter_index - x]+str(number_index - x)] == "b" or board[alphabet[letter_index - x]+str(number_index - x)] == "k" or board[alphabet[letter_index - x]+str(number_index - x)] == "q" or board[alphabet[letter_index - x]+str(number_index - x)] == "p":
                break
            else:
                m_NW.append(alphabet[letter_index - x] + str(number_index - x))
        m.append([m_NE,m_SE,m_SW,m_NW])
        return m

    if board[key] == "q":
        m = []
        m_north = []
        m_south = []
        m_east = []
        m_west = []
        m_NE = []
        m_SE = []
        m_SW = []
        m_NW = []
        n_dist = number_index-1
        e_dist = 7-letter_index
        s_dist = 8-number_index
        w_dist = letter_index 
        for x in range(1, min(n_dist,e_dist)+1):
            if board[alphabet[letter_index + x]+str(number_index - x)] == "r" or board[alphabet[letter_index + x]+str(number_index - x)] == "n" or board[alphabet[letter_index + x]+str(number_index - x)] == "b" or board[alphabet[letter_index + x]+str(number_index - x)] == "k" or board[alphabet[letter_index + x]+str(number_index - x)] == "q" or board[alphabet[letter_index + x]+str(number_index - x)] == "p":          
                break
            else:
                m_NE.append(alphabet[letter_index + x] + str(number_index - x))
        for x in range(1, min(s_dist,e_dist)+1):
            if board[alphabet[letter_index + x]+str(number_index + x)] == "r" or board[alphabet[letter_index + x]+str(number_index + x)] == "n" or board[alphabet[letter_index + x]+str(number_index + x)] == "b" or board[alphabet[letter_index + x]+str(number_index + x)] == "k" or board[alphabet[letter_index + x]+str(number_index + x)] == "q" or board[alphabet[letter_index + x]+str(number_index + x)] == "p":
                break
            else:
                m_SE.append(alphabet[letter_index + x] + str(number_index + x))
        for x in range(1, min(s_dist,w_dist)+1):
            if board[alphabet[letter_index - x]+str(number_index + x)] == "r" or board[alphabet[letter_index - x]+str(number_index + x)] == "n" or board[alphabet[letter_index - x]+str(number_index + x)] == "b" or board[alphabet[letter_index - x]+str(number_index + x)] == "k" or board[alphabet[letter_index - x]+str(number_index + x)] == "q" or board[alphabet[letter_index - x]+str(number_index + x)] == "p":
                break
            else:
                m_SW.append(alphabet[letter_index - x] + str(number_index + x))
        for x in range(1, min(n_dist,w_dist)+1):
            if board[alphabet[letter_index - x]+str(number_index - x)] == "r" or board[alphabet[letter_index - x]+str(number_index - x)] == "n" or board[alphabet[letter_index - x]+str(number_index - x)] == "b" or board[alphabet[letter_index - x]+str(number_index - x)] == "k" or board[alphabet[letter_index - x]+str(number_index - x)] == "q" or board[alphabet[letter_index - x]+str(number_index - x)] == "p":
                break
            else:
                m_NW.append(alphabet[letter_index - x] + str(number_index - x))
        
        for x in range((-1*int(key[1]))+1,0):
            if board[key[0]+str(-1*x)] == "r" or board[key[0]+str(-1*x)] == "n" or board[key[0]+str(-1*x)] == "b" or board[key[0]+str(-1*x)] == "k" or board[key[0]+str(-1*x)] == "q" or board[key[0]+str(-1*x)] == "p":
                break
            else:
                m_north.append(key[0]+str(-1*x))
        for x in range(int(key[1])+1,9):
            if board[key[0]+str(x)] == "r" or board[key[0]+str(x)] == "n" or board[key[0]+str(x)] == "b" or board[key[0]+str(x)] == "k" or board[key[0]+str(x)] == "q" or board[key[0]+str(x)] == "p":    
                break
            else:
                m_south.append(key[0]+str(x))
        for x in range(alphabet.index(key[0])+1,8):
            if board[alphabet[x]+key[1]] == "r" or board[alphabet[x]+key[1]] == "n" or board[alphabet[x]+key[1]] == "b" or board[alphabet[x]+key[1]] == "k" or board[alphabet[x]+key[1]] == "q" or board[alphabet[x]+key[1]] == "p":
                break
            else:
                m_east.append(alphabet[x]+key[1])
        for x in range((-1*alphabet.index(key[0]))+1,1):
            if board[alphabet[-1*x]+key[1]] == "r" or board[alphabet[-1*x]+key[1]] == "n" or board[alphabet[-1*x]+key[1]] == "b" or board[alphabet[-1*x]+key[1]] == "k" or board[alphabet[-1*x]+key[1]] == "q" or board[alphabet[-1*x]+key[1]] == "p":    
                break
            else:
                m_west.append(alphabet[-1*x]+key[1])
        m.append([m_north,m_east,m_south,m_west,m_NE,m_SE,m_SW,m_NW])
        return m

    pass



def move(a,b):  
    board[b]=board[a]
    board[a]="."


