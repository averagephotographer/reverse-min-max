import numpy as np

winner = False

def print_board(board):
    for row in board:
        print(row)
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
    x,y = p
    adjacent_points = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),             (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
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
    


# use adjacent points to determine the direction
def get_next(p1, p2):
    dir = get_dir(p1, p2)
    return go_dir(p2, dir)


# start with every current player point
# check if there is an adjacent point of the opposite color
# keep going in that direction until reaching zeroes or out of bounds
# if 0, then that is a legal move
# if null, that is not a move
def get_valid_moves(board, is_white_turn):
    # returns an array of tuples with possible moves
    w, b, e = locations(board)
    available_moves = []
    # can only play when there is one piece of the other color adjacent
    if (is_white_turn):
        # for every white point on the board
        for w_piece in w:
            # get all adjacent points for that point
            adj = adjacent_points(w_piece)
            # for every opposite color point on the board
            for b_piece in b:
                # if the opposite color is adjacent
                if b_piece in adj:
                    # get the next point
                    next_point = get_next(w_piece, b_piece)

                    # if the next point is in the same direction
                    # keep going until next_point is in zeroes or not existing
                    
                    # new start point
                    start_point = b_piece

                    # if the start point is a black piece
                    while start_point in b:
                        if next_point in e:
                            available_moves.append(next_point)
                            break

                        # while the next point is a black piece
                        while next_point in b:
                            new = get_next(start_point, next_point)
                            start_point = next_point
                            next_point = new

                            
    return available_moves
                                        
    # if curr_color is adject to iself, then adjacent to opp_color
    
    pass

while(winner == False):
    # print board 
    board_py = [
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    # white = 1
    # black = 2
    board_py[3][4] = 1
    board_py[4][3] = 1
    board_py[3][3] = 2
    board_py[4][4] = 2

    print_board(board_py)

    print(get_valid_moves(board_py, True))

    
    winner = True





