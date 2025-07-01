from .constants import ROWS,COLS,SQUARE_SIZE,WHITE,GREEN,BLACK
import pygame
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0

        self.create_board()

    def draw_squares(self,WINDOW):
        WINDOW.fill(BLACK)
        for i in range(ROWS):
            for j in range((i+1) % 2, COLS,2):
                x,y = j*SQUARE_SIZE,i*SQUARE_SIZE

                pygame.draw.rect(WINDOW,GREEN,(x,y,SQUARE_SIZE,SQUARE_SIZE))


    def create_board(self):
        from .pieces import Pieces

        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):

                if  0<= row <= 2 and (row + col)%2:
                    self.board[row].append(Pieces(row,col,BLACK))
                elif 5 <= row <= 7 and (row + col) %2:
                    self.board[row].append(Pieces(row,col,WHITE))
                else:
                    self.board[row].append(None)

            
    def draw_pieces(self,WINDOW):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is not None:
                    self.board[row][col].draw(WINDOW)

    def draw(self,WINDOW):
        self.draw_squares(WINDOW)
        self.draw_pieces(WINDOW)

               


