import pygame
from .board import Board
from .constants import WHITE,BLACK,SQUARE_SIZE,ROWS,COLS,WIDTH,HEIGHT
from .pieces import Pieces
def get_row_col(pos):
    x,y = pos
    return y//SQUARE_SIZE,x//SQUARE_SIZE



class Game:
    def __init__(self,WINDOW):
        
        self.window = WINDOW
        self.moves = {}
        self.selected_piece = None
        self.locked_piece = None

        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
        self.progression = 0

        self.board = Board()

        self.capture_moves = None
        self.piece = None
        self.moves = None
    #HANDLES USER CLICKS
    def handle_click(self,square):
        #Executes capturing a piece
        while self.capture_moves and self.piece and  square in self.capture_moves:

                    self.capture_piece(self.capture_moves,self.piece)
  
                    self.update()
                    if not self.piece:
                        return
                    self.capture_moves = self.piece.get_capture_moves(self.board.board)

                    self.locked_piece = self.piece
                    if not self.capture_moves:
                        self.piece.check_if_king(self.piece.row,self.board)
                        self.piece = None
                        self.locked_piece = None
                        self.board.swap_turn()
                    self.capture_moves = None
        #Executes moving a piece
        if self.moves and square in self.moves and self.piece:

            self.make_move(self.moves,self.piece)
            self.update()
            self.piece = None
            self.moves = None

        else:                
            self.update()
            self.piece = self.select_turn_piece(square[0],square[1])
            #Assures that during chain capturing other piece isn't chosen
            if self.locked_piece and self.piece != self.locked_piece:
                self.piece = None
                return                  
            if self.piece and self.piece.color == self.board.turn:
                
                capturing_pieces = self.get_all_capturing_pieces()
                if capturing_pieces:

                    self.capture_moves = self.piece.get_capture_moves(self.board.board)
                    if self.capture_moves:

                        self.piece.show_capture_moves(self.window,self.capture_moves)
                        self.moves = None
                else:
                    
                    self.moves = self.show_moves(self.piece)
    

    def update(self):
        self.board.draw(self.window)
    
    def get_selected_piece(self,row,col):
        if self.board.board[row][col]:
            return self.board.board[row][col]
        
    def select_turn_piece(self,row,col):
        if self.board.board[row][col] and self.board.board[row][col].color == self.board.turn:
            return self.board.board[row][col]






    def show_moves(self,piece):
        moves = piece.get_moves(self.board.board)
        piece.show_move(self.window,moves)
        return moves

    def show_capturing_moves(self,piece):
          return piece.show_capturing_moves(self.window,self.board.board)
    

    def make_move(self,moves,piece):
        new_board = piece.make_move(moves,self.board)
        if new_board:
            self.progression+=1
            self.board.set_progression(self.progression)
            self.board.swap_turn()

    def capture_piece(self,capture_moves,piece):
        new_board,color,became_king = piece.capture_piece(capture_moves,self.board)

        if new_board:
            if color == WHITE:
                self.white_left-=1
                self.board.set_white_left(self.white_left)
            else:
                self.black_left-=1
                self.board.set_black_left(self.black_left)
            self.progression = 0
            self.board.set_progression(self.progression)
            if became_king:
                self.piece = None
                self.locked_piece = None
                self.board.swap_turn()
                self.capture_moves = None
                return

    def get_all_capturing_pieces(self):
        pieces = []
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.board[row][col]
                if piece and piece.color == self.board.turn:
                    if piece.get_capture_moves(self.board.board):
                        pieces.append(piece)
        return pieces
    
    def display_win(self):
        win = self.board.check_win()
        if win == 1:
            self.display_TEXT("WHITE is Winner !!!")
            return True
        elif win == 2:
            self.display_TEXT("BLACK is Winner !!!")
            return True
        

    def display_no_legal_moves(self):
        if self.board.check_no_legal_moves():
            color = "WHITE" if WHITE != self.board.turn else "BLACK"
            self.display_TEXT(color + " is Winner") 
            return True

    def display_tie(self):
        if self.board.check_tie():
            self.display_TEXT("It's a Tie")
            return True

    def display_TEXT(self,winner_text):
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render(winner_text, True, (255, 255, 255))
        self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)


    def ai_move(self, board):
        self.board = board
        board.swap_turn()   
    
