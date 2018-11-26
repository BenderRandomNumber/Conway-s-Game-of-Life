import Conways_Game_of_Life.TheGameOfLifeV1 as CG1
import Conways_Game_of_Life.TheGameOfLifeV2 as CG2
import numpy as np
import cv2


'Still life Patterns:'

block = np.array([[1, 1],
                  [1, 1]])

tub = np.array([[0, 1, 0],
               [1, 0, 1],
               [0, 1, 0]])

boat = np.array([[1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]])


'Spaceship Patterns:'

glider = np.array([[0, 0, 1],
                   [1, 0, 1],
                   [0, 1, 1]])

spaceship = np.array([[0, 0, 1, 1, 0],
                     [1, 1, 0, 1, 1],
                     [1, 1, 1, 1, 0],
                     [0, 1, 1, 0, 0]])

lwss = np.array([[0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 0]])

mwss = np.array([[0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 0]])

hwss = np.array([[0, 0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 0]])

GosoperGliderGun = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

UFO = np.array([[0, 1, 1, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0]])


'Oscillators Patterns:'

quad_blinker = np.array([[0, 1, 0],
                        [1, 1, 1]])

blinker = np.array([[1],
                    [1],
                    [1]])

small_exploder = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [1, 0, 1],
                           [0, 1, 0]])

pulsar = np.array([[1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1]])

ten_cell_row = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

beacon = np.array([[1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 1, 1],
                   [0, 0, 1, 1]])


'misc Patterns:'

die_hard = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                   [1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 1, 1, 1]])

r_pentomino = np.array([[0, 1, 1],
                       [1, 1, 0],
                       [0, 1, 0]])

acorn = np.array([[0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [1, 1, 0, 0, 1, 1, 1]])

my_name = np.array([[1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]])

'Random Patterns'

def create_random_pattern(size):
    random = np.random.randint(0, 2, size)
    return random


'Img to Pattern:'

def Img_to_Patern(img):
    img_a = cv2.imread(img)
    print(img_a)
    pattern = img_a[:, :, 0] + img_a[:, :, 1] + img_a[:, :, 2]
    pattern = ((np.nan_to_num((pattern/pattern))) - 1) * -1
    pattern = pattern.astype(np.int64)
    return pattern


'Play!!!:'
def center_pattern(size, pattern):
    board_middle = (np.asarray(size) / 2).astype(np.int64)
    pattern_middle = (np.asarray(pattern.shape) / 2).astype(np.int64)

    board = np.zeros(size)
    board[board_middle[0] - pattern_middle[0]: board_middle[0] + pattern_middle[0] + (pattern.shape[0] % 2), board_middle[1] - pattern_middle[1]: board_middle[1] + pattern_middle[1] + (pattern.shape[1] % 2)] = pattern

    return board

def place_pattern(size, pos, pattern):
    board = np.zeros(size)
    board[pos[0]: pos[0] + pattern.shape[0], pos[1]: pos[1] + pattern.shape[1]] = pattern

    return board


test_board = center_pattern((20, 20), ten_cell_row)

CG2.play(test_board, -1, (255, 0, 0), (0, 0, 0), 1, 10)


