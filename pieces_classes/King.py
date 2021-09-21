class K:

    def __init__(self,position=0,colour="white",capture=False):
        """
        -------------------------------------------------------
        Initializes A King  class
        Use: node = bb(value)
        -------------------------------------------------------
        Parameters:
            colour-the colour of the piece
            position-the location of the piece on board
            capture-determines if a piece has been captured()
        Returns:
            A King object (_BST_Node)            
        -------------------------------------------------------
        """
     
        self._colour = colour
        self._position = position
        self._capture=capture

    def __repr__(self):
        if self._colour=="white":
            return "WK"
        else:
            return "BK"

    def __str__ (self):
        if self._colour=="white":
            return "WK"
        else:
            return "BK"
    
    def position_update(self,value):
        self._position=value

        return

    def current_position(self):
        return self._position