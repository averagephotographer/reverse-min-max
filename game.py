from time import sleep
import pygame
import sys

from pygame.constants import MOUSEBUTTONDOWN

from reversi import move

class Game():
    
    def __init__(self):
        
        pygame.init()

        # pygame board info
        self.size = self.width, self.height = 800, 800
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (50, 205, 50)
        self.gray = (128, 128, 128)
        self.screen = pygame.display.set_mode(self.size)


        # background board info
        self.white_turn = True

        self.board = [
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]]
        
        # self.board = [
        #     [1, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 1, 1, 1, 1, 1, 2, 1],
        #     [1, 1, 2, 2, 1, 2, 1, 1],
        #     [1, 1, 2, 1, 1, 1, 1, 1],
        #     [1, 1, 2, 1, 2, 2, 1, 1],
        #     [2, 1, 2, 2, 1, 1, 1, 1],
        #     [0, 0, 2, 1, 1, 1, 1, 1]]

        self.board_state = []
        
        self.w_pieces = []
        self.b_pieces = []
        self.zeros = []
        
    def setup(self):
        self.screen.fill(self.green)
        self._draw_lines()
        self.default_board()
        self.update_locations()
    
    def _draw_lines(self):
        # draws board lines
        for i in range(8):
            vert_distance  = self.height / 8
            # | | | (100, 0), (200, 0), etc.
            start_vert = (vert_distance * (i+1) , 0)
            # (100, 700), (200, 700), etc.
            end_vert = (vert_distance * (i+1), self.height)

            horiz_distance = self.width / 8
            # this needs to be (0, 100), (0, 200), etc.
            start_horiz = (0, horiz_distance * (i+1))
            # this needs to be (700, 100)
            end_horiz = (self.width, horiz_distance * (i+1))

            pygame.draw.line(self.screen, self.black, start_vert, end_vert, 1)
            pygame.draw.line(self.screen, self.black, start_horiz, end_horiz, 1)

    def default_board(self):
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[3][3] = 2
        self.board[4][4] = 2

    def save_board(self):
        self.board_state.append(self.board)

    def update_locations(self):
        self.w_pieces = []
        self.b_pieces = []
        self.zeros = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    self.w_pieces.append((i, j))
                elif self.board[i][j] == 2:
                    self.b_pieces.append((i, j))
                else:
                    self.zeros.append((i, j))
    
    def adjacent_points(self, p):
        i,j = p
        adjacent_points = [
            (i-1, j-1), (i, j-1), (i+1, j-1),
            (i-1, j),             (i+1, j),
            (i-1, j+1), (i, j+1), (i+1, j+1)
        ]   
        return adjacent_points
                    

    def get_dir(self, p1, p2):
        adj_p1 = self.adjacent_points(p1)

        if p2 == adj_p1[0]:
            return "NW"
        elif p2 == adj_p1[1]:
            return "N"
        elif p2 == adj_p1[2]:
            return "NE"
        elif p2 == adj_p1[3]:
            return "W"
        elif p2 == adj_p1[4]:
            return "E"
        elif p2 == adj_p1[5]:
            return "SW"
        elif p2 == adj_p1[6]:
            return "S"
        elif p2 == adj_p1[7]:
            return "SE"
        else:
            print("not adjacent")
            return None
        

    def go_dir(self, point, direction):
        adj = self.adjacent_points(point)
        if direction == "NW":
            return adj[0] 
        elif direction == "N":
            return adj[1] 
        elif direction == "NE":
            return adj[2] 
        elif direction == "W":
            return adj[3] 
        elif direction == "E":
            return adj[4] 
        elif direction == "SW":
            return adj[5] 
        elif direction == "S":
            return adj[6]
        elif direction == "SE":
            return adj[7]
        else:
            print("not a direction")
            return None
        
    # gets the next point in the direction the pieces are oriented
    def get_next(self, p1, p2):
        dir = self.get_dir(p1, p2)
        return self.go_dir(p2, dir)

    
    # input a start point (assuming it is a valid move)
    # output rays to update the board with
    def make_rays(self, start):
        rays_array = []
        adj = self.adjacent_points(start)

        if (self.white_turn):
            atkr, opp, empty = self.w_pieces, self.b_pieces, self.zeros
        else:
            opp, atkr, empty = self.w_pieces, self.b_pieces, self.zeros
        # for every adjacent point
        for point in adj:
            # if the point is an opposing piece
            if point in opp:
                # continue down that point
                head = point
                tail = start

                temp_array = []

                while head in opp:
                    temp_array.append(head)
                    next = self.get_next(tail, head)
                    tail = head
                    head = next

                    if head in atkr:
                        rays_array.append(temp_array)
                        break
                    if head in empty:
                        break
        return rays_array


    def move(self, location):
        
        valid = self.get_valid_moves()
        
        if location in valid:
            # change spot
            height, width = location
            if self.white_turn:
                value = 1
                self.board[height][width] = value
            else:
                value = 2
                self.board[height][width] = value
            
            # update all possible rays
            rays = self.make_rays(location)
            for ray in rays:
                for point in ray:
                    x, y = point
                    self.board[x][y] = value
        else:
            raise Exception("Invalid move")


    # start with every current player point
    # check if there is an adjacent point of the opposite color
    # keep going in that direction until reaching zeroes or out of bounds
    # if 0, then that is a legal move
    # if null, that is not a move
    def get_valid_moves(self):
        # returns an array of tuples with possible moves
        if (self.white_turn):
            atkr, opp, empty = self.w_pieces, self.b_pieces, self.zeros

        else:
            opp, atkr, empty = self.w_pieces, self.b_pieces, self.zeros
        available_moves = []
        
        # can only play when there is one piece of the other color adjacent
        # for every white point on the board
        for att_piece in atkr:
            # get all adjacent points for that point
            adj = self.adjacent_points(att_piece)
            # for every opposite color point on the board
            for tail in opp:
                # if the opposite color is adjacent
                if tail in adj:
                    # get the next point
                    head = self.get_next(att_piece, tail)
                    # if the next point is in the same direction
                    # keep going until next_point is in zeroes or not existing
                    
                    # if the start point is an opposing piece
                    while tail in opp:
                        # if the next point is empty
                        if head in atkr:
                            break
                        if head in empty:
                            # set that point as an available move
                            if head not in available_moves:
                                available_moves.append(head)
                            break
                        if head not in opp:
                            break

                        # if the next point is an opposing tile
                        # continue until there are no more
                        while head in opp:
                            new = self.get_next(tail, head)
                            tail = head
                            head = new
                            if head in empty:
                                if head not in available_moves:
                                    available_moves.append(head)
                                break
        return available_moves


    def tup_mul(self, t1, t2):
        x1, y1 = t1
        x2, y2 = t2
        result = ( x1*x2, y1*y2 )
        return result

    def tup_add(self, t1, t2):
        x1, y1 = t1
        x2, y2 = t2
        result = ( x1+x2, y1+y2 )
        return result


    def place_piece(self, grid_pos, color, width=0):
        # size of square in the grid
        square_size = (self.width/8, self.height/8) 
        
        # gets the position of the grid in the game
        game_pos = self.tup_mul(square_size, grid_pos)
        
        # pygame places the center of the circle at the point
        # offest moves the point from a grid intersection to the center of square
        offset = self.tup_mul(square_size, (.5, .5))

        # updates the game position
        game_pos = self.tup_add(game_pos, offset)

        # gets radius from the defined square size
        Bx, _ = square_size
        rad = round(Bx / 2.5) # w/o the division, the circle would be 4x the size of square

        pygame.draw.circle(self.screen, color, game_pos, rad, width)
    
    def game_is_over(self):
        if len(self.get_valid_moves()) == 0:
            self.white_turn = not self.white_turn
            if len(self.get_valid_moves()) == 0:
                return True
        return False 
    
    def transpose(self):
        n = len(self.board)
        result = [[row[i] for row in self.board] for i in range(n)]
        return result

    def print_board(self):
        t_posed = self.transpose()
        print("   0, 1, 2, 3, 4, 5, 6, 7 ")
        
        for row in range(len(t_posed)):
            print(row, end=' ')
            print(t_posed[row])
        print()

    def convert_pos(self, mouse_pos):
        x, y = mouse_pos
        return int(x/100), int(y/100)


    def place_all(self):
        for piece in self.w_pieces:
            self.place_piece(piece, self.white)
        for piece in self.b_pieces:
            self.place_piece(piece, self.black)
        for piece in self.zeros:
            self.place_piece(piece, self.green)
    
    # stackoverflow.com/a/47112546/16369768
    def play(self):
        clock = pygame.time.Clock()
        self.setup()
        playing = True
        self.update_locations()
        self.place_all()
        avail = self.get_valid_moves()
        print(avail)

        for potential in avail:
            self.place_piece(potential, self.gray)
    

        while(playing):
            
            clock.tick(15)  # fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    new_pos = self.convert_pos(pos)

                    print("isvalid: {}".format(new_pos in avail))
                    if new_pos in avail:
                        potential = []
                        print(new_pos)

                        self.move(new_pos)
                        self.print_board()

                        self.update_locations()
                        self.place_all()

                        self.white_turn = not self.white_turn
                        avail = self.get_valid_moves()
                        print(avail)
                        
                        if len(avail) == 0:
                            if self.white_turn:
                                print("white pass")
                            else:
                                print("black pass")
                            self.white_turn = not self.white_turn
                            avail = self.get_valid_moves()
                            if len(avail) == 0:
                                print("no avail moves, game over")
                                break                        

                        for potential in avail:
                            self.place_piece(potential, self.gray)

                        
                        if self.white_turn:
                            print("white turn")
                        else:
                            print("black turn")


            pygame.display.update()
            


            

game = Game()
game.play()

