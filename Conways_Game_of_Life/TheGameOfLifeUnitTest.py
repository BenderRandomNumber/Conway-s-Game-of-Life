import Conways_Game_of_Life.TheGameOfLife as CG
import numpy as np


'Still life Patterns:'

block = np.array([[1, 1],
                  [1, 1]])

tub = np.array([[0, 1, 0],
               [1, 0, 1],
               [0, 1, 0]])


'Spaceship Patterns:'

glider = np.array([[0, 0, 1],
                   [1, 0, 1],
                   [0, 1, 1]])

ship = np.array([[1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1],
                 [0, 1, 1, 1, 1]])

GosoperGliderGun = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])


'Oscillators Patterns:'

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

'Random Patterns'

def create_random_pattern(size):
    random = np.random.randint(0, 2, size)
    return random



def play_patter(pattern):
    starting_board = np.zeros((100, 100), np.int64)
    starting_board[int((starting_board.shape[0]/2) - (pattern.shape[0]/2)) : int((starting_board.shape[0]/2) + (pattern.shape[0]/2)), int((starting_board.shape[1]/2) - (pattern.shape[1]/2)) : int((starting_board.shape[1]/2) + (pattern.shape[1]/2))] = pattern
    CG.TheGameOfLife.play_game(starting_board, -1, 1000, 10)


play_patter(GosoperGliderGun)
