import pygame
import sys

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


def place_piece(grid_pos, color):
    blocksize = (width/7, height/7) 
    game_pos = tup_mul(blocksize, grid_pos)
    offset = tup_mul(blocksize, (.5, .5))
    game_pos = tup_add(game_pos, offset)
    Bx, By = blocksize
    rad = round(Bx / 2.5)

    pygame.draw.circle(screen, color, game_pos, rad)

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0 , 0)
green = (50,205,50)

screen.fill(green)

# draws lines
for i in range(7):
    vert_distance  = height / 7
    # | | | (100, 0), (200, 0), etc.
    start_vert = (vert_distance * (i+1) , 0)
    # (100, 700), (200, 700), etc.
    end_vert = (vert_distance * (i+1), height)

    horiz_distance = width / 7
    # this needs to be (0, 100), (0, 200), etc.
    start_horiz = (0, horiz_distance * (i+1))
    # this needs to be (700, 100)
    end_horiz = (width, horiz_distance * (i+1))

    pygame.draw.line(screen, black, start_vert, end_vert, 1)
    pygame.draw.line(screen, black, start_horiz, end_horiz, 1)


running = True
while(True):
    place_piece((0,0), white)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


