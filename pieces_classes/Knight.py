class N:

    def __init__(self,position=0,colour="white",capture=False):
        """
        -------------------------------------------------------
        Initializes a Knight class
        Use: node = bb(value)
        -------------------------------------------------------
        Parameters:
            colour-the colour of the piece
            position-the location of the piece on board
            capture-determines if a piece has been captured()
        Returns:
            A Knight object (_BST_Node)            
        -------------------------------------------------------
        """
     
        self._colour = colour
        self._position = position
        self._capture = capture

    def __repr__(self):
        if self._colour=="white":
            return "WN"
        else:
            return "BN"

    def __str__ (self):
        if self._colour=="white":
            return "WN"
        else:
            return "BN"

    def which_colour(self,colour):
        return self._colour
    
    def position_update(self,value):
        self._position=value

        return
    
    def current_position(self):
        return self._position