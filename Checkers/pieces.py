from .constants import RADIUS_PIECE,RADIUS_MOVE,BLACK,WHITE,BLUE,SQUARE_SIZE,COLS,ROWS
import pygame
class Pieces:
    def __init__(self,row,col,color):
        self.king = False
        self.row = row
        self.col = col
        self.color = color

        if self.king:
            self.directions = 0
        else:
            self.directions = 1 if color == BLACK else -1
            pass
    
    def draw(self,WINDOW):
        #Center of the circle of piece
        x,y = self.col * SQUARE_SIZE + SQUARE_SIZE//2,self.row * SQUARE_SIZE + SQUARE_SIZE//2

        pygame.draw.circle(WINDOW,self.color,[x,y],RADIUS_PIECE,0)


    def draw_possible_move(self,WINDOW,row,col):
        x,y = col * SQUARE_SIZE + SQUARE_SIZE//2,row * SQUARE_SIZE + SQUARE_SIZE//2

        pygame.draw.circle(WINDOW,BLUE,[x,y],RADIUS_MOVE,0)

    def show_move(self,WINDOW,board):
        print(self.row,self.col,self.directions)
        moves = []
        if 0 <= self.row + self.directions < ROWS:
            if self.col - 1 >= 0:
                row,col = self.row + self.directions,self.col - 1
                if board[row][col] is None:
                    moves.append((row,col))
                    self.draw_possible_move(WINDOW,row,col)
            if self.col + 1 < COLS:
                row,col = self.row + self.directions,self.col + 1
                if board[row][col] is None:
                    moves.append((row,col))
                    self.draw_possible_move(WINDOW,row,col)
        return moves
    def __repr__(self):
        return str(self.color)