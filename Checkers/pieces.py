from .constants import RADIUS_PIECE,RADIUS_MOVE,BLACK,WHITE,BLUE,SQUARE_SIZE,COLS,ROWS,CROWN
import pygame
class Pieces:
    def __init__(self,row,col,color):
        self.king = False
        self.row = row
        self.col = col
        self.color = color

        if self.king:
            self.directions = [1,-1]
        else:
            self.directions = [1] if color == BLACK else [-1]
            pass
    
    def draw(self,WINDOW):
        #Center of the circle of piece
        x,y = self.col * SQUARE_SIZE + SQUARE_SIZE//2,self.row * SQUARE_SIZE + SQUARE_SIZE//2

        pygame.draw.circle(WINDOW,self.color,[x,y],RADIUS_PIECE,0)

        if self.king:
            WINDOW.blit(CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))


    def draw_possible_move(self,WINDOW,row,col):
        x,y = col * SQUARE_SIZE + SQUARE_SIZE//2,row * SQUARE_SIZE + SQUARE_SIZE//2

        pygame.draw.circle(WINDOW,BLUE,[x,y],RADIUS_MOVE,0)

    def get_move(self,board):
        moves = []
        for direction in self.directions:
            if 0 <= self.row + direction < ROWS:
                if self.col - 1 >= 0:
                    row,col = self.row + direction,self.col - 1
                    if board[row][col] is None:
                        moves.append((row,col))
                if self.col + 1 < COLS:
                    row,col = self.row + direction,self.col + 1
                    if board[row][col] is None:
                        moves.append((row,col))
        return moves

    def show_move(self,WINDOW,moves):

        for row,col in moves:
            self.draw_possible_move(WINDOW,row,col)
            self.draw_possible_move(WINDOW,row,col)
    

    
    def get_capture_moves(self,board):
        capturing_moves = {}

        for direction in self.directions:
            #LEFT CAPTURE
            middle_row = self.row + direction
            middle_col = self.col - 1
            landing_row = self.row + direction * 2
            landing_col = self.col - 2
            if 0 <= landing_row < ROWS and 0 <= landing_col < COLS:
                middle_piece = board[middle_row][middle_col]
                if middle_piece and middle_piece.color != self.color:
                    if board[landing_row][landing_col] is None:
                        capturing_moves[(landing_row,landing_col)] = (middle_row,middle_col)


            #RIGHT CAPTURE
            middle_row = self.row + direction
            middle_col = self.col + 1
            landing_row = self.row + direction * 2
            landing_col = self.col + 2
            if 0 <= landing_row < ROWS and 0 <= landing_col < COLS:
                middle_piece = board[middle_row][middle_col]
                if middle_piece and middle_piece.color != self.color:
                    if board[landing_row][landing_col] is None:
                        capturing_moves[(landing_row,landing_col)] = (middle_row,middle_col)            
        
        return capturing_moves
    
    def show_capture_moves(self,WINDOW,capture_moves):
        for key in capture_moves.keys():
            self.draw_possible_move(WINDOW, key[0], key[1])



    def check_if_king(self,row):
        if self.color == BLACK and row == 7:
            self.directions = [-1,1]
            self.king = True

        if self.color == WHITE and row == 0:
            self.directions = [-1,1]
            self.king = True
    
    def crown_a_king(self,WINDOW):
        center_x,center_y = self.col * SQUARE_SIZE + SQUARE_SIZE//2 , self.row * SQUARE_SIZE + SQUARE_SIZE//2
        WINDOW.blit(CROWN,(center_x - CROWN.get_width()//2,center_y - CROWN.get_height()//2))

    
    def __repr__(self):
        return str(self.color)