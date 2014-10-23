#!/usr/bin/python3
__author__ = 'Cole'

#Copyright Cole Gosney 2014
#Tetrus (not tetris, obv)

import pygame
import sys
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 375))
pygame.display.set_caption("Tetris")

myfont = pygame.font.SysFont("monospace", 15)

board = [[0] * 10 for _ in range(15)]

block_list = []

current_block = []

print_asci_dict = {'L':['I', 'I', 'I__'],
                   'J':['  I', '  I', '__I'],
                   'I':['I', 'I', 'I', 'I'],
                   'T':['  I', 'I I I'],
                   'F_Z':['--', ' --'],
                   'B_Z':[' --', '--'],
                   'O':[' ___', '[   ]', '[___]']}

tetrimoes_num_dict = {'L':2,
                   'J':3,
                   'I':4,
                   'T':5,
                   'F_Z':6,
                   'B_Z':7,
                   'O':8}

score = 0

landed = False

start = False

class colors:
    black = pygame.Color(0, 0, 0)
    orange = pygame.Color(255, 127, 0)
    cyan = pygame.Color(0, 255, 255)
    lime = pygame.Color(191, 255, 0)
    amber = pygame.Color(255, 191, 0)
    yellow = pygame.Color(255, 255, 0)
    red = pygame.Color(255, 0, 0)
    magenta = pygame.Color(255, 0, 255)
    white = pygame.Color(255, 255, 255)

def get_coords(block):
    coords = []
    if block[0] == 'L':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] + 1, block[3] + 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] - 1, block[3] + 1])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] - 1, block[3] - 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] - 1])
    elif block[0] == 'J':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] - 1, block[3] + 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3] - 1])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] + 1, block[3] - 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
    elif block[0] == 'I':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2], block[3] + 2])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 2, block[3]])
        if block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] - 2])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] - 2, block[3]])
    elif block[0] == 'T':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2], block[3] - 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] + 1, block[3]])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2], block[3] + 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] - 1, block[3]])
    elif block[0] == 'F_Z':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] + 1, block[3] + 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] - 1, block[3] + 1])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] + 1, block[3] + 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] - 1, block[3]])
            coords.append([block[2] - 1, block[3] + 1])
    elif block[0] == 'B_Z':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] - 1, block[3] + 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2], block[3] + 1])
            coords.append([block[2] - 1, block[3] + 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2], block[3] - 1])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
    elif block[0] == 'O':
        if block[1] == 1:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
            coords.append([block[2], block[3] + 1])
        elif block[1] == 2:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
            coords.append([block[2], block[3] + 1])
        elif block[1] == 3:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
            coords.append([block[2], block[3] + 1])
        elif block[1] == 4:
            coords.append([block[2], block[3]])
            coords.append([block[2] + 1, block[3]])
            coords.append([block[2] + 1, block[3] + 1])
            coords.append([block[2], block[3] + 1])
    return coords

def draw_blocks():
    for a in range(0, 15):
        for b in range(0, 10):
            color_dict = {1: colors.black,
                          2: colors.red,
                          3: colors.cyan,
                          4: colors.orange,
                          5: colors.lime,
                          6: colors.amber,
                          7: colors.magenta,
                          8: colors.yellow}
            if board[a][b]:
                pygame.draw.rect(screen, color_dict[board[a][b]],
                                    (b * 25, a * 25, 25, 25))

def check_line():
    global landed, score
    num_lines = 0
    temp = True
    if len(current_block) != 0:
        for a in range(0, 15):
            for b in range(0, 10):
                if board[a][b] != 0:
                    temp = True
                else:
                    temp = False
                    break
            if temp and landed:
                for b in range(0, 10):
                    board[a][b] = 0
                num_lines += 1
    for i in range(0, num_lines):
        score += 1
        for a in range(1, 16):
            for b in range(0, 10):
                if 15 - a != 14 and board[15 - a][b] != 0 and board[15 - a + 1][b] == 0:
                    board[15 - a + 1][b] = board[15 - a][b]
                    board[15 - a][b] = 0
    return num_lines

def update():
    global landed
    temp = False
    print(check_line())
    if len(current_block) != 0 and len(current_block) == 6:
        coords = get_coords(current_block)
        for i in coords:
            if i[1] == 14:
                print("dead1")
                temp = False
                break
            elif board[i[1] + 1][i[0]] != 0 and [i[0], i[1] + 1] not in coords:
                print("dead2")
                temp = False
                break
            else:
                temp = True
        if temp and current_block[5] % 30 == 0:
            for i in coords:
                board[i[1]][i[0]] = 0
            current_block[3] += 1
            new_coords = get_coords(current_block)
            for i in new_coords:
                board[i[1]][i[0]] = tetrimoes_num_dict[current_block[0]]
        elif not temp:
            if current_block[4] and current_block[5] % 10 == 0:
                current_block.remove(current_block[0])
                current_block.remove(current_block[0])
                current_block.remove(current_block[0])
                current_block.remove(current_block[0])
                current_block.remove(current_block[0])
                current_block.remove(current_block[0])
                landed = True
            elif not current_block[4]:
                current_block[4] = True
                current_block[5] = 0
    else:
        for i in current_block:
            current_block.remove(current_block[0])

def gen_game_list(number_of_tetrimos):
    tetrimos = {0:'L', 1:'J', 2:'I', 3:'T', 4:'F_Z', 5:'B_Z', 6:'O'}
    tetrimos_list = []
    for i in range(0, number_of_tetrimos):
        tetrimos_list.append(tetrimos[random.randint(0, 6)])
    print(tetrimos_list)
    return tetrimos_list

def reset():
    global board, block_list, current_block, score, print_asci_dict, landed, start
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    block_list = []

    current_block = []

    score = 0

    print_asci_dict = {'L':['I', 'I', 'I__'],
                       'J':['  I', '  I', '__I'],
                       'I':['I', 'I', 'I', 'I'],
                       'T':['  I', 'I I I'],
                       'F_Z':['--', ' --'],
                       'B_Z':[' --', '--'],
                       'O':[' ___', '[   ]', '[___]']}

    landed = False

    start = False

while True:
    screen.fill(colors.white)

    if start:
        reset_wanted = False

        if len(current_block) != 0:
            current_block[len(current_block) - 1] += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    current_block = ['L', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_s:
                    current_block = ['J', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_d:
                    current_block = ['I', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_f:
                    current_block = ['T', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_g:
                    current_block = ['F_Z', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_h:
                    current_block = ['B_Z', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_j:
                    current_block = ['O', 1, 5, 2, False, 0]
                    landed = False
                elif event.key == K_r:
                    reset_wanted = True
                elif event.key == K_SPACE:
                    if len(current_block) != 0:
                        temp_block = []
                        for i in current_block:
                            temp_block.append(i)
                        if temp_block[1] == 4:
                            temp_block[1] = 1
                        else:
                            temp_block[1] += 1
                        coords = get_coords(current_block)
                        temp_coords = get_coords(temp_block)
                        temp = False
                        count = 0
                        for a in temp_coords:
                            for b in a:
                                not_on_bottom = True
                                if b > 14:
                                    not_on_bottom = False
                                if b > 9 and count % 2 == 0:
                                    temp = False
                                    break
                                elif b < 0 and count % 2 == 0:
                                    temp = False
                                    break
                                elif b > 14 and count % 2 == 1:
                                    temp = False
                                    break
                                elif b < 14 and count % 2 == 1:
                                    if board[a[1]][a[0]] != 0 and [a[0], a[1]] not in coords:
                                        temp = False
                                        break
                                else:
                                    temp = True
                                count += 1
                            if not temp:
                                break
                        if temp:
                            coords = get_coords(current_block)
                            for i in coords:
                                board[i[1]][i[0]] = 0
                            if current_block[1] == 4:
                                current_block[1] = 1
                            else:
                                current_block[1] += 1
                            coords = get_coords(current_block)
                            for i in coords:
                                board[i[1]][i[0]] = tetrimoes_num_dict[current_block[0]]
                elif event.key == K_LEFT:
                    if len(current_block) != 0:
                        coords = get_coords(current_block)
                        temp = False
                        count = 0
                        for a in coords:
                            for b in a:
                                if b == 0 and count % 2 == 0:
                                    temp = False
                                    break
                                elif board[a[1]][a[0] - 1] != 0 and [a[0] - 1, a[1]] not in coords:
                                    temp = False
                                    break
                                else:
                                    temp = True
                                count += 1
                            if not temp:
                                break
                        if temp:
                            for i in coords:
                                board[i[1]][i[0]] = 0
                            current_block[2] -= 1
                            coords = get_coords(current_block)
                            for i in coords:
                                board[i[1]][i[0]] = tetrimoes_num_dict[current_block[0]]
                elif event.key == K_RIGHT:
                    if len(current_block) != 0:
                        coords = get_coords(current_block)
                        temp = False
                        count = 0
                        for a in coords:
                            for b in a:
                                if b == 9 and count % 2 == 0:
                                    temp = False
                                    break
                                elif board[a[1]][a[0] + 1] != 0 and [a[0] + 1, a[1]] not in coords:
                                    temp = False
                                    break
                                else:
                                    temp = True
                                count += 1
                            if not temp:
                                break
                        if temp:
                            for i in coords:
                                board[i[1]][i[0]] = 0
                            current_block[2] += 1
                            coords = get_coords(current_block)
                            for i in coords:
                                board[i[1]][i[0]] = tetrimoes_num_dict[current_block[0]]
                elif event.key == K_DOWN:
                    if len(current_block) != 0:
                        coords = get_coords(current_block)
                        temp = False
                        count = 0
                        for a in coords:
                            for b in a:
                                if b == 14 and count % 2 == 1:
                                    temp = False
                                    break
                                elif b < 14 and count % 2 == 1:
                                    if board[a[1] + 1][a[0]] != 0 and [a[0], a[1] + 1] not in coords:
                                        temp = False
                                        break
                                else:
                                    temp = True
                                count += 1
                            if not temp:
                                break
                        if temp:
                            for i in coords:
                                board[i[1]][i[0]] = 0
                            current_block[3] += 1
                            coords = get_coords(current_block)
                            for i in coords:
                                board[i[1]][i[0]] = tetrimoes_num_dict[current_block[0]]
        update()

        draw_blocks()

        temp = 0

        for i in print_asci_dict[block_list[0]]:
            temp += 1
            screen.blit(myfont.render(str(i), 1, (0,0,0)), (255, (250 + (15 * temp))))

        screen.blit(myfont.render(str(score), 1, (0,0,0)), (255, 100))

        if len(current_block) == 0 and len(block_list) != 0:
            current_block = [block_list[0], 1, 5, 2, False, 0]
            update()
            landed = False
            block_list.remove(block_list[0])

        print(current_block)

        if reset_wanted:
            reset()
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start = True
                    block_list = gen_game_list(200)

        lines = ["space = play or rotate",
                 "left = move left",
                 "right = move right",
                 "r = restart"]
        for line, y_value in zip(lines, range(150, 291, 20)):
            screen.blit(myfont.render(line, 1, (0, 0, 0)), (10, y_value))

    pygame.display.update()
    clock.tick(30)
