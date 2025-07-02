import pygame
from .board import Board
from .constants import WHITE,BLACK,SQUARE_SIZE,ROWS,COLS

def get_row_col(pos):
    x,y = pos
    return y//SQUARE_SIZE,x//SQUARE_SIZE

def swap_turn(game):
    if game.turn == WHITE:
        game.turn = BLACK
    else:
        game.turn = WHITE

class Game:
    def __init__(self,WINDOW):
        
        self.window = WINDOW
        self.turn = WHITE
        self.moves = {}
        self.selected_piece = None

        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0

        self.board = Board()


    def update(self):
        self.board.draw(self.window)
    
    def get_selected_piece(self,row,col):
        if self.board.board[row][col]:
            return self.board.board[row][col]

        return None
    



    def show_moves(self,piece):
        return piece.show_move(self.window,self.board.board)

    def show_capturing_moves(self,piece):
          return piece.show_capturing_moves(self.window,self.board.board)

    def make_move(self,moves,piece):
        row,col = get_row_col(pygame.mouse.get_pos())
        print(moves)
        if (row,col) in moves:
            self.board.board[row][col] = piece
            self.board.board[piece.row][piece.col] = None
            piece.row,piece.col = row,col

            swap_turn(self)
        return
    
    def capture_piece(self,capture_moves,piece):
        row,col = get_row_col(pygame.mouse.get_pos())

        if (row,col) in capture_moves.keys():
            captured_piece_row,captured_piece_col = capture_moves[(row,col)]
            captured_piece = self.get_selected_piece(captured_piece_row,captured_piece_col)
            if captured_piece.color == WHITE:
                self.white_left-=1
            else:
                self.black_left-=1

            self.board.board[captured_piece.row][captured_piece.col] = None
            self.board.board[piece.row][piece.col] = None
            self.board.board[row][col] = piece
            piece.row,piece.col = row,col
            return True
        else:
            return False

    def get_all_capturing_pieces(self):
        pieces = []
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.board[row][col]
                if piece and piece.color == self.turn:
                    if piece.get_capture_moves(self.board.board):
                        pieces.append(piece)
        return pieces
    
    
