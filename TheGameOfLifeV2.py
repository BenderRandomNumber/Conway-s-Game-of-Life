import numpy as np
import cv2


def find_x(a):
    x = np.arange(0, a.shape[1])
    x = np.tile(x, a.shape[0]).reshape(a.shape)
    return x


def find_y(a):
    y = np.arange(0, a.shape[0])
    y = np.repeat(y, a.shape[1]).reshape(a.shape)
    return y


def find_neighbors_num(array, r):
    new_A = np.zeros((array.shape[0] + 1, array.shape[1] + 1))
    new_A[1:, 1:] = array

    X = find_x(new_A)
    Y = find_y(new_A)
    R = (np.ones(new_A.shape) * r).astype(np.int64)

    def find_neighbors(x, y, range):
        min_x = x - range
        max_x = x + range + 1
        min_y = y - range
        max_y = y + range + 1
        return np.sum((new_A[min_y: max_y, min_x: max_x])) - new_A[y, x]

    vf = np.vectorize(find_neighbors)

    return vf(X, Y, R)[1:, 1:]


def update_board(board_array):
    neighbor_num = find_neighbors_num(board_array, 1)
    alive = neighbor_num * board_array
    dead = neighbor_num * (board_array == 0)

    alive = (2 <= alive) * (alive <= 3)
    dead = dead == 3

    updated_array = (alive + dead)

    return updated_array.astype(np.int64)


def show_board(board_array, wait_time, alive_rgb, dead_rgb):
    new_array = np.repeat(board_array, 3).reshape((board_array.shape[0] * board_array.shape[1], 3))
    alive = (new_array == 0) * alive_rgb
    dead = (new_array == 1) * dead_rgb
    new_array = dead + alive

    array_img = np.reshape(new_array, (board_array.shape[0], board_array.shape[1], 3)).astype(np.uint8)
    cv2.imshow("The Game of Life", array_img)
    cv2.waitKey(wait_time)


def play(starting_array, max_gen, dead_color, alive_color, waitTime):
    a_rgb = np.asarray(dead_color)
    d_rgb = np.asarray(alive_color)
    previous_array = starting_array
    array = update_board(previous_array)
    i = 0
    done = False
    while not done:
        show_board(previous_array, waitTime, a_rgb, d_rgb)
        previous_array = array
        array = update_board(previous_array)
        if i == max_gen:
            done = True
        i += 1

