import pygame
from .board import Board
from .constants import WHITE,BLACK,SQUARE_SIZE

def get_row_col(pos):
    x,y = pos
    return y//SQUARE_SIZE,x//SQUARE_SIZE

class Game:
    def __init__(self,WINDOW):
        
        self.window = WINDOW
        self.turn = WHITE
        self.moves = {}
        self.selected_piece = None
        self.board = Board()


    def update(self):
        self.board.draw(self.window)
    
    def get_selected_piece(self,row,col):
        if self.board.board[row][col]:
            return self.board.board[row][col]

        return None

    def show_moves(self,piece):
        return piece.show_move(self.window,self.board.board)  

    def make_move(self,moves,piece):
        row,col = get_row_col(pygame.mouse.get_pos())
        print(moves)
        if (row,col) in moves:
            self.board.board[row][col] = piece
            self.board.board[piece.row][piece.col] = None
            piece.row,piece.col = row,col
        return