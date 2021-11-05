import numpy as np


board_py = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

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

def move(location, is_white):
    height, width = location
    if is_white:
        board_py[height][width] = 1
    else:
        board_py[height][width] = 2
    

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
                        # if the next point is empty
                        if next_point in e:
                            # set that point as an available move
                            available_moves.append(next_point)
                            break

                        # if the next point is a black tile
                        # continue until there are no more
                        while next_point in b:
                            new = get_next(start_point, next_point)
                            start_point = next_point
                            next_point = new
                            if next_point in e:
                                available_moves.append(next_point)
                                break
    return available_moves
                                        
def main():
    winner = False

    while(winner == False):
        # white = 1
        # black = 2

        # standard setup
        # move((3, 4), True)
        # move((4, 3), True)
        # move((3, 3), False)
        # move((4, 4), False)

        # height x width coordinate system
        move((3,3), False)
        move((4,3), False)
        move((5,3), False)
        move((4,4), False)
        move((3,4), True)

        
        print_board(board_py)

        print(get_valid_moves(board_py, True))
        
        winner = True

if __name__ == "__main__":
    main()





