from Bishop import B
from King import K
from Rook import R
from Knight import N
from Queen import Q
from empty_space import X

class P:

    def __init__(self,position=0,colour="White",capture=False,two_step=False):
        """
        -------------------------------------------------------
        Initializes a Pawn class
        Use: node = bb(value)
        -------------------------------------------------------
        Parameters:
            colour-the colour of the piece
            position-the location of the piece on board
            capture-determines if a piece has been captured()
        Returns:
            A Pawn object (object)            
        -------------------------------------------------------
        """
     
        self._colour = colour
        self._position = position
        self._capture=capture

    def __repr__(self):
        if self._colour=="White":
            return "WP"
        else:
            return "BP"

    def __str__ (self):
        if self._colour=="White":
            return "WP"
        else:
            return "BP"

    def position_update(self,value):
        self._position=value

        return

    def which_colour(self):
        return self._colour

    def current_position(self):
        return self._position
    
    def rules(self,initial_position,board,final_position,side,take_piece):
        signal=False
        moving_lane=initial_position[0]

        if (moving_lane-1==final_position[0] and initial_position[1] == final_position[1] and self._colour=="White" and side=='W' and isinstance(take_piece,X)==True) or \
            (moving_lane-1==final_position[0] and initial_position[1] == final_position[1] and self._colour=="black" and side=='B' and isinstance(take_piece,X)==True):
            signal=True
        elif (isinstance(take_piece,X)==False and moving_lane-1==final_position[0] and (initial_position[1]-1==final_position[1] or initial_position[1]+1==final_position[1]) and self._colour=="White" and side=='W' and take_piece._colour=="black") or\
            (isinstance(take_piece,X)==False and moving_lane-1==final_position[0] and (initial_position[1]-1==final_position[1] or initial_position[1]+1==final_position[1]) and self._colour=="black" and side=='B' and take_piece._colour=="White") :
            signal=True

        else:
            signal=False

        

        return signal



