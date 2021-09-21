from Bishop import B
from King import K
from Knight import N
from Queen import Q
from empty_space import X

class R:

    def __init__(self,position=0,colour="white",capture=False):
        """
        -------------------------------------------------------
        Initializes a Rook class
        Use: node = bb(value)
        -------------------------------------------------------
        Parameters:
            colour-the colour of the piece
            position-the location of the piece on board
            capture-determines if a piece has been captured()
        Returns:
            A Rook object (_BST_Node)            
        -------------------------------------------------------
        """
     
        self._colour = colour
        self._position = None
        self._capture=capture

    def __repr__(self):
        if self._colour=="white":
            return "WR"
        else:
            return "BR"

    def __str__ (self):
        if self._colour=="white":
            return "WR"
        else:
            return "BR"

    def position_update(self,value):
        self._position=value

        return


    def which_colour(self):
        return self._colour
        
    def current_position(self):
        return self._position

    def rules(self,initial_position,board,final_position,side,take_piece):
        signal=False
        inital_pos1=initial_position[0]
        inital_pos2=initial_position[1]

        final_pos1=final_position[0]
        final_pos2=final_position[1]

        if inital_pos1!=final_pos1:
 
            check= self.lane_check(initial_position,board,final_position,side)

            if check ==True:
                signal=True
            else:
                signal=False
 
        elif inital_pos2!=final_pos2:
            check= self.lane_check(initial_position,board,final_position,side)
            if check ==True:
                signal=True
            else:
                signal=False
        else:
            signal=False

        



        return signal

    def lane_check(self,initial_position,board,final_position,side):
        
        check=False
        breaker=False

        if initial_position[0]<final_position[0]and breaker==False:
            counter=initial_position[0]


            while counter<final_position[0]:
                position_checker= board[counter+1][initial_position[1]]
                
                if isinstance(position_checker,X)==True:
                    counter+=1
                    breaker=False

                    check=True 
                else:
                    check=False
                    breaker=True


        elif initial_position[0]>final_position[0]:
            counter=initial_position[0]


            while counter>final_position[0] and breaker==False:
                position_checker= board[counter-1][initial_position[1]]
                print("hello")
                if isinstance(position_checker,X)==True:
                    counter-=1
                    breaker=False

                    check=True 
                else:
                    check=False
                    breaker=True

        elif initial_position[1]<final_position[1]:
            counter=initial_position[1]

            while counter<final_position[1]and breaker==False:
                position_checker= board[initial_position[0]][counter+1]
                
                if isinstance(position_checker,X)==True:
                    counter+=1
                    breaker=False

                    check=True 
                else:
                    check=False
                    breaker=True

        elif initial_position[1]> final_position[1]:
            counter=initial_position[1]

            while counter>final_position[1] and breaker==False:
                position_checker= board[initial_position[0]][counter-1]
                
                if isinstance(position_checker,X)==True:
                    counter-=1
                    breaker=False

                    check=True 
                else:
                    check=False
                    breaker=True





        return check
