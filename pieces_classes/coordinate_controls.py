from Bishop import B
from King import K
from Rook import R
from Knight import N
from Queen import Q
from empty_space import X


#Bank that is used to convert from number qoordinates of list to text coordinates"
conversion_bank={
    (7,0):"A1",(7,1):"B1",(7,2):'C1',(7,3):"D1",
(7,4):"E1",(7,5):"F1",(7,6):"G1",(7,7):"H1",(6,0):"A2",(6,1):"B2",(6,2):"C2",(6,3):"D2",
(6,4):"E2",(6,5):"F2",(6,6):"G2",(6,7):"H2",(5,0):"A3",(5,1):"B3",(5,2):"C3",(5,3):"D3",
(5,4):"E3",(5,5):"F3",(5,6):"G3",(5,7):"H3",(4,0):"A4",(4,1):"B4",(4,2):"C4",(4,3):"D4",
(4,4):"E4",(4,5):"F4",(4,6):"G4",(4,7):"H4",(3,0):"A5",(3,1):"B5",(3,2):"C5",(3,3):"D5",
(3,4):"E5",(3,5):"F5",(3,6):"G5",(3,7):"H5",(2,0):"A6",(2,1):"B6",(2,2):"C6",(2,3):"D6",
(2,4):"E6",(2,5):"F6",(2,6):"G6",(2,7):"H6",(1,0):"A7",(1,1):"B7",(1,2):"C7",(1,3):"D7",
(1,4):"E7",(1,5):"F7",(1,6):"G7",(1,7):"H7",(0,0):"A8",(0,1):"B8",(0,2):"C8",(0,3):"D8",
(0,4):"E8",(0,5):"F8",(0,6):"G8",(0,7):"H8"

}


def numbers_to_coordinates(board):
    """
    -------------------------------------------------------
    Function which goes through a list containing chess pieces
    and converts the nested list indexes into chess board positions, 
    which are then stored by each of the individual chess piece objects
    example: ((0,4) ----> "E8")
    Use: numbers_to_coordinates(chess_board)
    -------------------------------------------------------
    Parameters:
        board- a list containing the chess board(list)
    Returns:
        None          
    -------------------------------------------------------
    """

    for i in board: # Iterating through all 8 rows of the board (The outer lists)
        
        indexs=board.index(i) # Storing the index of the current row being worked with
        for j in i: # iteraring through each individual piece/square of the current row (iterating through each value of the inner list)
            inner_index=i.index(j) # Storing the index of the current piece/square being worked with
            real_index=(indexs,inner_index) #creating a tuple using the index of the row and square respectivly (outer list, inner list)

            if real_index in conversion_bank: # checking to make sure that the index created is valid
                j.position_update(conversion_bank[real_index]) # Fetching the corresponding chess board position from the conversion bank
                                                               # and assigning the position to the piece/square

            #print(j.current_position()) # Testing positions (self use)
            #print(j)
            #print("----------------")



    return

def qoordinate_to_number(qoordinate):
    """
    -------------------------------------------------------
    Function which goes through a list containing chess pieces
    and converts the chess board positions into nested list indexes
    example: ("E8" ----> (0,4))
    Use: qoordinate_to_number(qoordinate)
    -------------------------------------------------------
    Parameters:
        qoordinate- a singular coordinate string (list)
    Returns:
        Tuple representing the nested list index of a particular piece (tuple)          
    -------------------------------------------------------
    """
    key_list = list(conversion_bank.keys()) # Making a list of all the nested listed positions stored in the conversion bank
    val_list = list(conversion_bank.values()) # Making a list of all the chess board positions stored in the conversion bank

    position = val_list.index(qoordinate) # Takes given qoordinate ex. "A1", and locates it in the list of chess board positions, storing
                                          # the index of the position in the variable


    key = key_list[position] # Using the index of the chess board position, the value of the nested list index is found 
                             #(As both key and value were stored in the lists before, the corresponding positions are in the same location, in each list)

    return key  # Returning the value of the nested list position for the peice chess board position that was entered


def move_piece(initial_key,board,final_key,side):
    """
    -------------------------------------------------------
    Function which is used to move pieces on the chess board.
    -------------------------------------------------------
    Parameters: 
        initial_key: the key of the piece to be moved (tuple)
        board: the chess board on which all the pieces are located (list)
        final_key: the key of the position that the piece will be moved to (tuple)

    Returns:
        None
    -------------------------------------------------------
    """
     # Checking if rule is passed for a particular piece, if so, true, else false

    piece=board[initial_key[0]][initial_key[1]] # The intial tuple is taken and split into to parts which is then used to access the list for the
                                                # peice that is to be moved.
    
    take_piece=board[final_key[0]][final_key[1]]
    rule=piece.rules(initial_key,board,final_key,side,take_piece)                          # Checking if rule is passed for a particular piece, if so, true, else false
    print(take_piece)
    print(piece)
    print(rule)
    print(type(X()))
    print(type(take_piece))
    print(isinstance(take_piece,X))






    if take_piece==X():
        print("hello")


    if rule==True: #check to see if rules of pieces are passed, if the rule does not pass then false returned
        old_space=X() #empty space object created which will be placed in the old position of the piece being moved
        moving_piece=piece  #Piece to be moved is stored in a variable, which will then be placed into the new position on the board
        board[initial_key[0]][initial_key[1]]=old_space # Adding an empty space to the spot where the piece being moved used to be
        board[final_key[0]][final_key[1]]=moving_piece # Placing the moved piece in the new position

        numbers_to_coordinates(board) # Reset all chess piece positions
    else:
        print(piece.which_colour())
        print("This move is not allowed")
    
    return



def move_piece_aux():
    initial_key=input("What is the position of the piece that you would like to move: ")
    final_key=input("What is the final position you would like to move that piece to: ")

    initial_key= qoordinate_to_number(initial_key)
    print(initial_key)
    final_key= qoordinate_to_number(final_key)
    print(final_key)



    return initial_key,final_key
