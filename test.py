from tetromino import Tetromino
from i import Ipiece
from o import Opiece
from s import Spiece
from z import Zpiece
from j import Jpiece
from l import Lpiece
from k import Kpiece
import pygame
from pygame import mixer
import random
import os

# Gets random shape out of all the different tetrominos
def get_shape():
    arr = []
    i = Ipiece([[0,3],[0,4],[0,5],[0,6]],(115,208,225),False) # Light Blue, Long Piece
    o = Opiece([[0,4],[0,5],[1,4],[1,5]],(252,223,  3),False) # Yellow, Square Piece
    s = Spiece([[0,4],[1,4],[1,5],[2,5]],(144,252,  3),False) # Green, Step Piece
    z = Zpiece([[0,5],[1,5],[1,4],[2,4]],(252, 65,  3),False) # Red, Step Piece
    j = Jpiece([[0,5],[1,5],[1,4],[1,3]],(237,123, 24),False) # Orange, J Piece
    l = Lpiece([[0,3],[1,3],[1,4],[1,5]],(0  , 44,156),False) # Dark Blue, L Piece
    k = Kpiece([[0,4],[1,3],[1,4],[1,5]],(177, 24,237),False) # Purple, Pyramid Piece

    arr.append(i)
    arr.append(o)
    arr.append(s)
    arr.append(z)
    arr.append(j)
    arr.append(k)
    arr.append(l)
    return random.choice(arr)

# As tetromino falls it replaces the previous position with black
def remove_current(grid, piece):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if [i,j] in piece.coords:
                grid[i][j] = (0,0,0)

# Given coordinates it dispays whether or not the coordinates are valid on the grid
def valid_space(shape, grid):
    pos = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == (0,0,0):
                pos += [[i,j]]

    for i in range(len(shape.coords)):
        if shape.coords[i] not in pos:
            return False
    return True

# Creates the grid using the dictionary places to determine the places where there is a tetromino
def create_grid(places):
    grid = [[(0,0,0) for _ in range(10)]for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) in places:
                key = places[(i,j)]
                grid[i][j] = key
    return grid

# Draws the actual grid pattern
def draw_grid(screen, grid):
    for i in range(len(grid)):
        pygame.draw.line(screen, (128,128,128), (0, 50+i*block_size), (p_width, 50+i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(screen, (128,128,128), (j*block_size, 50), (j*block_size, 50+p_height))

# Draws the held piece
def draw_hold(screen, hold):
    tetromino = {
        (115,208,225):[[0,3],[0,4],[0,5],[0,6]],
        (252,223,  3):[[0,4],[0,5],[1,4],[1,5]],
        (144,252,  3):[[0,4],[1,4],[1,5],[2,5]],
        (252, 65,  3):[[0,5],[1,5],[1,4],[2,4]],
        (237,123, 24):[[0,5],[1,5],[1,4],[1,3]],
        (0  , 44,156):[[0,3],[1,3],[1,4],[1,5]],
        (177, 24,237):[[0,4],[1,3],[1,4],[1,5]]
    }

    for value in tetromino:
        if hold.color == value:
            pygame.draw.rect(screen, hold.color, (tetromino[value][0][1]*(block_size-3)+260, tetromino[value][0][0]*(block_size-3)+87, block_size*.85, block_size*.85))
            pygame.draw.rect(screen, hold.color, (tetromino[value][1][1]*(block_size-3)+260, tetromino[value][1][0]*(block_size-3)+87, block_size*.85, block_size*.85))
            pygame.draw.rect(screen, hold.color, (tetromino[value][2][1]*(block_size-3)+260, tetromino[value][2][0]*(block_size-3)+87, block_size*.85, block_size*.85))
            pygame.draw.rect(screen, hold.color, (tetromino[value][3][1]*(block_size-3)+260, tetromino[value][3][0]*(block_size-3)+87, block_size*.85, block_size*.85))

# Draws everything else (Tetris, red border, score, etc)
def draw_window(screen, grid, s_width, score, hold):
    screen.fill(color)

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 50)
    label = font.render('Tetris', 1, (255,255,255))
    screen.blit(label, (s_width/2 - (label.get_width()/2), 0))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, grid[i][j], (j*block_size, 50 + i*block_size, block_size, block_size))

    draw_grid(screen, grid)
    pygame.draw.rect(screen, (255,0,0), (0, 50, p_width, p_height), 3)

    # Display Score
    font = pygame.font.SysFont('comicsans', 25)
    score = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score, (315, 190))

    # Draw Hold
    pygame.draw.rect(screen, (0,255,0), (320, 60, 120, 120), 8)
    if hold != None:
        draw_hold(screen, hold)

    pygame.display.update()

# Draws the actual piece falling (fills the color)
def draw_tetromino(grid, piece):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if [i,j] in piece.coords:
                grid[i][j] = piece.color
    pygame.display.update()

# When an entire row is filled up, this clear it
def removeRows(grid, places):
    places = {}
    add = 0
    for i in reversed(range(len(grid))):
        counter = 0
        for j in range(len(grid[i])):
            if grid[i][j] == (0,0,0):
                continue
            else:
                counter += 1
        if counter > 9:
            clear.play()
            grid.pop(i)
            add += 1

    replacement = [[(0,0,0) for _ in range(10)]for _ in range(add)]
    replacement += grid

    for i in range(len(replacement)):
        for j in range(len(replacement[i])):
            if replacement[i][j] == (0,0,0):
                continue
            else:
                p = (i,j)
                places[p] = replacement[i][j]

    points = add * 100
    if add == 2:
        points * 2
    if add == 3:
        points * 3
    if add == 4:
        points * 4
    return replacement, places, points

# Detects if gameover by checking if the pieces have went to 0
def gameover(places):
    for value in places:
        if value[0] <= 0:
            return True
    return False

# Main Code 
def main(screen, s_width):
    # All the variables needed 
    places = {}
    grid = create_grid(places)
    current_piece = get_shape()
    final_piece = current_piece
    next_piece = get_shape()
    while next_piece.color == current_piece.color:
        next_piece = get_shape()
    holdValue = 0
    hold = None
    change_piece = False
    change_hold = False
    amount = 1
    points = 0
    score = 0
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = .27
    run = True

    # Main loop
    while run:
        # Incremently drops the piece
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/2000 > fall_speed:
            fall_time = 0
            remove_current(grid, current_piece)
            current_piece.move_down()

            if not(valid_space(current_piece, grid)):
                current_piece.move_up()
                change_piece = True

        # Takes in all the player inputs (movement, holding)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False      

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # Move left
                    remove_current(grid, current_piece)
                    move.play()
                    current_piece.move_left()
                    # print(current_piece.coords)
                    if not (valid_space(current_piece, grid)):
                        current_piece.move_right()
                if event.key == pygame.K_RIGHT: # Move right
                    remove_current(grid, current_piece)
                    move.play()
                    current_piece.move_right()
                    # print(current_piece.coords)
                    if not (valid_space(current_piece, grid)):
                        current_piece.move_left()
                if event.key == pygame.K_DOWN: # tap to move down once
                    remove_current(grid, current_piece)
                    if valid_space(current_piece, grid):
                        current_piece.move_down()
                    else:
                        current_piece.move_up()
                if event.key == pygame.K_UP: # Rotate
                    remove_current(grid, current_piece)
                    rotate.play()
                    current_piece.rotate(amount)
                    # print(current_piece.coords)
                    amount += 1
                    amount %= 4
                if event.key == pygame.K_SPACE: # Drop down instantly
                    remove_current(grid, current_piece)
                    drop.play()
                    while (valid_space(current_piece, grid)):
                        current_piece.move_down()
                        # print(current_piece.coords)
                    current_piece.move_up()
                if event.key == pygame.K_c: # Hold piece
                    if not current_piece.been_held() and hold == None:
                        remove_current(grid, current_piece)
                        current_piece.held = True
                        current_piece.resetCoords()
                        hold = current_piece
                        change_hold = True
                    elif not current_piece.been_held() and hold != None and holdValue < 1:
                        current_piece.held = True
                        remove_current(grid, current_piece)
                        current_piece.resetCoords()
                        current_piece, hold = hold, current_piece
                        amount = 1

        # Changes to a new piece, when player holds
        if change_hold:
            current_piece = next_piece
            next_piece = get_shape()
            while next_piece.color == current_piece.color:
                next_piece = get_shape()
            amount = 1
            holdValue += 1
            change_hold = False

        # Changes to a new piece, when tetris piece has reached the bottom
        if change_piece:
            for coords in current_piece.coords:
                p = (coords[0], coords[1])
                places[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            while next_piece.color == current_piece.color:
                next_piece = get_shape()
            amount = 1
            holdValue = 0
            change_piece = False
            grid = create_grid(places)
            grid, places, points = removeRows(grid, places)
            score += points

        if gameover(places):
            run = False

        draw_tetromino(grid, current_piece)
        draw_window(screen, grid, s_width, score, hold)

# The resolution of the screen, the size of the grid,
s_width, s_height = 450, 700
p_width, p_height = 300, 600
cols, rows = 10, 24
block_size = p_width/cols
color = (0, 0, 0)

# All music added
mixer.init()
drop = pygame.mixer.Sound('music/drop.wav')
clear = pygame.mixer.Sound('music/clear.wav')
move = pygame.mixer.Sound('music/move.wav')
rotate = pygame.mixer.Sound('music/rotate.wav')
music = mixer.music.load('music/tetrisTheme.wav')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")

if __name__=="__main__":
    main(screen, s_width)