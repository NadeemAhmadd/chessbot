
from __future__ import print_function
from string import ascii_uppercase as letters
from Bishop import B
from Pawn import P
from King import K
from Rook import R
from Knight import N
from Queen import Q
from empty_space import X
from coordinate_controls import numbers_to_coordinates, move_piece

def chess_board_generator(side):
    if side=='W':
        a_h=list(letters[:8])
        index_num=iter(range(8,0,-1))
        



        chess_board=[["X" for i in range(8)]for i in range(8)]

        BP = [P(colour="black",two_step=True) for i in range(8)]
        WP = [P(two_step=True) for i in range(8)]
        chess_board[1]=BP
        chess_board[6]=WP

        BK = K(colour="black")
        WK = K()
        chess_board[7][4]=WK
        chess_board[0][4]=BK

        BR = [R(colour="black") for i in range(2)]
        WR = [R() for i in range(2)]
        chess_board[0][0]=BR[0]
        chess_board[0][7]=BR[1]
        chess_board[7][0]=WR[0]
        chess_board[7][7]=WR[1]

        BB = [B(colour="black") for i in range(2)]
        WB = [B() for i in range(2)]
        chess_board[0][2]=BB[0]
        chess_board[0][5]=BB[1]
        chess_board[7][2]=WB[0]
        chess_board[7][5]=WB[1]

        BN = [N(colour="black") for i in range(2)]
        WN = [N() for i in range(2)]
        chess_board[0][1]=BN[0]
        chess_board[0][6]=BN[1]
        chess_board[7][1]=WN[0]
        chess_board[7][6]=WN[1]

        BQ = [Q(colour="black") for i in range(2)]
        WQ = [Q() for i in range(2)]
        chess_board[0][3]=BQ[0]
        chess_board[7][3]=WQ[1]

        X1 = [X() for i in range(8)]
        X2 = [X() for i in range(8)]
        X3 = [X() for i in range(8)]
        X4 = [X() for i in range(8)]
        chess_board[2]=X1
        chess_board[3]=X2
        chess_board[4]=X3
        chess_board[5]=X4


        numbers_to_coordinates(chess_board)



        for i in chess_board:
            print("\n")
            print(next(index_num),end=" ")
            for j in i:
                print(j,end=" ")
        print("\n")
        print("  "+"  ".join(a_h))
        print("\n")
    else:
        index_num=iter(range(8,0,-1))
        a_h=list(letters[:8])
        



        chess_board=[["X" for i in range(8)]for i in range(8)]

        BP = [P(colour="black",two_step=True) for i in range(8)]
        WP = [P(two_step=True) for i in range(8)]
        chess_board[6]=BP
        chess_board[1]=WP

        BK = K(colour="black")
        WK = K()
        chess_board[7][4]=BK
        chess_board[0][4]=WK

        BR = [R(colour="black") for i in range(2)]
        WR = [R() for i in range(2)]
        chess_board[0][0]=WR[0]
        chess_board[0][7]=WR[1]
        chess_board[7][0]=BR[0]
        chess_board[7][7]=BR[1]

        BB = [B(colour="black") for i in range(2)]
        WB = [B() for i in range(2)]
        chess_board[0][2]=WB[0]
        chess_board[0][5]=WB[1]
        chess_board[7][2]=BB[0]
        chess_board[7][5]=BB[1]

        BN = [N(colour="black") for i in range(2)]
        WN = [N() for i in range(2)]
        chess_board[0][1]=WN[0]
        chess_board[0][6]=WN[1]
        chess_board[7][1]=BN[0]
        chess_board[7][6]=BN[1]

        BQ = [Q(colour="black") for i in range(2)]
        WQ = [Q() for i in range(2)]
        chess_board[0][3]=WQ[0]
        chess_board[7][3]=BQ[1]

        X1 = [X() for i in range(8)]
        X2 = [X() for i in range(8)]
        X3 = [X() for i in range(8)]
        X4 = [X() for i in range(8)]
        chess_board[2]=X1
        chess_board[3]=X2
        chess_board[4]=X3
        chess_board[5]=X4


        numbers_to_coordinates(chess_board)



        for i in chess_board:
            print("\n")
            print(next(index_num),end=" ")
            for j in i:
                print(j,end=" ")
        print("\n")
        print("  "+"  ".join(a_h))
        print("\n")
        
    return chess_board

def game_generator(chess_board,side):
    
    if side=="W":
        index_num=iter(range(8,0,-1))
        a_h=list(letters[:8])

        for i in chess_board:
            print("\n")
            print(next(index_num),end=" ")
            for j in i:
                print(j,end=" ")
        print("\n")
        print("  "+"  ".join(a_h))
        print("\n")
    else:
        index_num=iter(range(8,0,-1))
        a_h=list(letters[:8])

        for i in chess_board:
            print("\n")
            print(next(index_num),end=" ")
            for j in i:
                print(j,end=" ")
        print("\n")
        print("  "+"  ".join(a_h))
        print("\n")


    return

