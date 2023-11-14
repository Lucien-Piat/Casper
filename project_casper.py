import numpy as np


board = np.full([5, 5], fill_value=' ')

board[1,2]="A"


list_ascii = [ "O", "X"]



def print_board(list_ascii, board):
    for i in range(board.shape[0]):
        for y in range(board.shape[1]):
            print('[',board[i,y],"]  | ",sep="", end='')
        print('\n    |')
    
print_board(list_ascii, board)