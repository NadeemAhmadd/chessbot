from __future__ import print_function
from string import ascii_uppercase as letters
from Bishop import B
from Pawn import P
from King import K
from Rook import R
from Knight import N
from Queen import Q
from empty_space import X
from coordinate_controls import numbers_to_coordinates, move_piece, move_piece_aux
from chess import chess_board_generator,game_generator


signal=True
side=input("Which side would you like to play as. W for White, B for Black: ")

chess_board=chess_board_generator(side)
while signal:

    intial_key,final_key=move_piece_aux()
    move_piece(intial_key,chess_board,final_key,side)
    game_generator(chess_board,side)




