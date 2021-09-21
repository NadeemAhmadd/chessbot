class X:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes a Empty Space Class
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

    def __repr__(self):

            return "XO"

    def __str__ (self):

            return "XO"

    def position_update(self,value):
        self._position=value

        return

    def current_position(self):
        return self._position
