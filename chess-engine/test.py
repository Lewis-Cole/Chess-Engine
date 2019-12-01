# #testing here
from engine import board, moves, move
# import random

# for (keylewis,_) in board.items():
#     print(keylewis)
#     print(moves(keylewis))
#     print("---")
a=["A8","A7"]
for x in a: 
    if board[x] == "p" or board[x] == "r" or board[x] == "n" or board[x] == "b" or board[x] == "k" or board[x] == "q":
                a[a.index(x)]="."
                print "poo"
                

move("A8","A6")
print a
print board["A6"]
print moves("A7")
