from typing import Tuple


class Board():
    def __init__(self, board = None):
        # if initializing, setup the board normally
        if board != None:
            self = board
        else:
            self.brd = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0] ]
            self.setup_board()

    # modifies the print string
    # print(board_obj) prints a board nicely
    def __str__(self):
        myString = ""
        for row in self.brd:
            myString = "" + myString + str(row) + "\n"

        return myString
    
    # converts coordinate points to array index
    def cor_to_ind(self, coordinate):
        x, y = coordinate
        index_x = x - 1
        index_y = len(self.brd) - y

        return (index_y, index_x)

    def ind_to_cor(self, index):
        y, x = index

        cord_x = x + 1
        cord_y = -(y - len(self.brd))
        
        return (cord_x, cord_y)
    
    # given a piece at given coordinate
    # makes the board pieces have a normal coordinate system
    # with 0,0 at the bottom left
    def place(self, coordinate, is_white):
        ind = self.cor_to_ind(coordinate)
        ind_x, ind_y = ind

        # sets the piece depending on whose turn it is
        if is_white:
            value = 1
        else:
            value = 2
        
        self.brd[ind_x][ind_y] = value

    def setup_board(self):
        self.place((4, 4), True)
        self.place((5, 5), True)
        self.place((4, 5), False)
        self.place((5, 4), False)

    def get_pieces(self):
        # tuples to hold the positions of pieces
        white = []
        black = []
        empty = []
        
        # for each row
        for i in range(len(self.brd)):
            # for each item in the row
            for j in range(len(self.brd[0])):
                if self.brd[i][j] == 1:
                    white.append((i, j))
                if self.brd[i][j] == 2:
                    black.append((i,j))
                else:
                    empty.append((i, j))


class Player():
    # list of coordinates where the pieces are
    # list of potential moves
    # player can pass - whenever they can't move
    # player can move
    pass

class Game():
    def __init__(self):
        self.is_white = True
        self.valid_moves = []
        self.current_board = Board()
    
    def get_valid_moves(self):
        b, w, e = self.current_board.get_pieces()

    def move(self, coordinate):
        pass
    # can go to previous board
    # and make a potential next board

    # has the rules
    # valid moves


game = Game()



playing = True
while(playing):
    

    playing = False
