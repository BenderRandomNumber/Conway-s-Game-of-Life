import numpy as np
import cv2

class TheGameOfLife:
    @staticmethod
    def find_neighbors(row, column, board):
        neighbors = np.zeros(8, np.int64)
        directions = np.array([[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]])
        i = 0
        for direction in directions:
            new_row = row + direction[0]
            new_column = column + direction[1]

            new_row = new_row % len(board)
            new_column = new_column % len(board[0])
            new_val = board[new_row][new_column]

            neighbors[i] = new_val
            i += 1
        return neighbors

    @classmethod
    def find_num_of_neighbors(cls, row, column, board):
        neighbors = cls.find_neighbors(row, column, board)
        return int((np.nan_to_num((neighbors / neighbors))).sum())

    @staticmethod
    def alive(row, column, board):
        alive = True
        if board[row][column] == 0:
            alive = False
        return alive

    @classmethod
    def update_board(cls, board):
        updated_board = np.zeros(board.shape, np.int64)
        for row in range(len(board)):
            for column in range(len(board[0])):
                neighbor_num = cls.find_num_of_neighbors(row, column, board)
                alive = cls.alive(row, column, board)

                if not(alive):
                    if neighbor_num == 3:
                        new_val = 1
                    else:
                        new_val = 0
                else:
                    if 2 <= neighbor_num <= 3:
                        new_val = 1
                    else:
                        new_val = 0

                updated_board[row][column] = new_val

        return updated_board

    @staticmethod
    def show_board(board, scale, milliseconds):
        img_array = np.asarray((board.repeat(3).reshape((board.shape[0], board.shape[1], 3)) * 255), np.uint8)
        img_array = cv2.resize(img_array, dsize=(img_array.shape[1] * scale, img_array.shape[0] * scale),
                               interpolation=0)
        cv2.imshow("The Game of life", img_array)
        cv2.waitKey(milliseconds)

    @classmethod
    def play_game(cls, starting_board, max_gen, fps, scale):

        previous_board = starting_board
        board = cls.update_board(previous_board)

        done = False
        i = 0
        while not done:
            cls.show_board(previous_board, scale, int(1000 / fps))

            previous_board = board
            board = cls.update_board(previous_board)

            if i == max_gen:
                done = True

            if cv2.waitKey(1) & 0xFF == ord('q'):
                done = True

            i += 1

        cv2.destroyAllWindows()
