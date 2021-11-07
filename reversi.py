import pygame
import sys
# white = 1, True
# black = 2, False
board_py = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

# board_py = [
    # [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    # [ 1, 1, 1, 0, 0, 0, 0, 0 ],
    # [ 0, 0, 2, 0, 0, 0, 0, 0 ],
    # [ 0, 0, 1, 2, 1, 0, 0, 0 ],
    # [ 0, 0, 0, 1, 2, 0, 0, 0 ],
    # [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    # [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    # [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

def print_board(board):
    print("   0, 1, 2, 3, 4, 5, 6, 7 ")
    for row in range(len(board)):
        print(row, end=' ')
        print(board[row])
    print()


# python board
def locations(board):
    ones = []
    twos = []
    zeros = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                ones.append((i, j))
            elif board[i][j] == 2:
                twos.append((i, j))
            else:
                zeros.append((i, j))

    return ones, twos, zeros

def adjacent_points(p): 
    i,j = p
    adjacent_points = [
        (i-1, j-1), (i, j-1), (i+1, j-1),
        (i-1, j),             (i+1, j),
        (i-1, j+1), (i, j+1), (i+1, j+1)
    ]   
    return adjacent_points


def get_dir(p1, p2):
    adj_p1 = adjacent_points(p1)

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
    

def go_dir(point, direction):
    adj = adjacent_points(point)
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
def get_next(p1, p2):
    dir = get_dir(p1, p2)
    return go_dir(p2, dir)

# input a start point (assuming it is a valid move)
# output rays to update the board with
def make_rays(start, is_white_turn):
    ray_array = []
    adj = adjacent_points(start)

    if (is_white_turn):
        atkr, opp, empty = locations(board_py)
    else:
        opp, atkr, empty = locations(board_py)

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
                next = get_next(tail, head)
                tail = head
                head = next

                if head in atkr:
                    ray_array.append(temp_array)
                    break

    return ray_array



def move(location, is_white):
    
    valid = get_valid_moves(board_py, is_white)
    
    if location in valid:
        # change spot
        height, width = location
        if is_white:
            value = 1
            board_py[height][width] = value
        else:
            value = 2
            board_py[height][width] = value
        
        # update all possible rays
        rays = make_rays(location, is_white)
        for ray in rays:
            for point in ray:
                x, y = point
                board_py[x][y] = value
    else:
        raise Exception("Invalid move")
        
    
# start with every current player point
# check if there is an adjacent point of the opposite color
# keep going in that direction until reaching zeroes or out of bounds
# if 0, then that is a legal move
# if null, that is not a move
def get_valid_moves(board, is_white_turn):
    # returns an array of tuples with possible moves
    if (is_white_turn):
        atkr, opp, empty = locations(board)

    else:
        opp, atkr, empty = locations(board)
    available_moves = []
    
    # can only play when there is one piece of the other color adjacent
    # for every white point on the board
    for att_piece in atkr:
        # get all adjacent points for that point
        adj = adjacent_points(att_piece)
        # for every opposite color point on the board
        for tail in opp:
            # if the opposite color is adjacent
            if tail in adj:
                # get the next point
                head = get_next(att_piece, tail)
                # if the next point is in the same direction
                # keep going until next_point is in zeroes or not existing
                
                # if the start point is an opp piece
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
                    # if the next point is a black tile
                    # continue until there are no more
                    while head in opp:
                        new = get_next(tail, head)
                        tail = head
                        head = new
                        if head in empty:
                            if head not in available_moves:
                                available_moves.append(head)
                            break
    return available_moves


def default_setup():
    # standard setup
    board_py[3][4] = 1
    board_py[4][3] = 1
    board_py[3][3] = 2
    board_py[4][4] = 2
                     
def tup_mul(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    result = ( x1*x2, y1*y2 )
    return result

def tup_add(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    result = ( x1+x2, y1+y2 )
    return result


def place_piece(screen, dimensions, grid_pos, color, width=0):
    width, height = dimensions
    blocksize = (width/8, height/8) 
    game_pos = tup_mul(blocksize, grid_pos)
    offset = tup_mul(blocksize, (.5, .5))
    game_pos = tup_add(game_pos, offset)
    Bx, By = blocksize
    rad = round(Bx / 2.5)

    pygame.draw.circle(screen, color, game_pos, rad, width)

def game():
    white_turn = True
    
    # setup board array
    default_setup()
    
    pygame.init()
    screen = pygame.display.set_mode(size)

    size = width, height = 800, 800
    white = (255, 255, 255)
    black = (0, 0 , 0)
    green = (50,205,50)
    light_green = (128, 128, 128)
    

    screen.fill(green)

    # draws lines
    for i in range(8):
        vert_distance  = height / 8
        # | | | (100, 0), (200, 0), etc.
        start_vert = (vert_distance * (i+1) , 0)
        # (100, 700), (200, 700), etc.
        end_vert = (vert_distance * (i+1), height)

        horiz_distance = width / 8
        # this needs to be (0, 100), (0, 200), etc.
        start_horiz = (0, horiz_distance * (i+1))
        # this needs to be (700, 100)
        end_horiz = (width, horiz_distance * (i+1))

        pygame.draw.line(screen, black, start_vert, end_vert, 1)
        pygame.draw.line(screen, black, start_horiz, end_horiz, 1)

    
    
    # update board
    # display valid moves

    running = True
    while(True):
        # if both players pass
        if len(get_valid_moves(board_py, white_turn)) == 0:
            white_turn = not white_turn
            if len(get_valid_moves(board_py, white_turn)) == 0:
                print("\n game over")
                return

        # before turn
        att, opp, zer = locations(board_py)
        for piece in att:
            place_piece(screen, size, piece, white)
        for piece in opp:
            place_piece(screen, size, piece, black)

        avail = get_valid_moves(board_py, white_turn)

        for potential in avail:
            place_piece(screen, size, potential, light_green, 1)
            

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

def main():
    white_turn = False
    # default_setup()

    while(True):
        if len(get_valid_moves(board_py, white_turn)) == 0:
            white_turn = not white_turn
            print("\npass")
            if len(get_valid_moves(board_py, white_turn)) == 0:
                print("\n game over")
                return

        print_board(board_py)
        print(get_valid_moves(board_py, white_turn))

        if white_turn:
            print("\nWhite turn")
        else:
            print("\nBlack turn")
        
        x = int(input("your x: "))
        y = int(input("your y: "))

        # height x width coordinate system
        move((x, y), white_turn)

        if (white_turn == True):
            white_turn = False
        else:
            white_turn = True


    
if __name__ == "__main__":
    game()
    # main()





