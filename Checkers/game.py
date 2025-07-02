import pygame
from .board import Board
from .constants import WHITE,BLACK,SQUARE_SIZE,ROWS,COLS,WIDTH,HEIGHT

def get_row_col(pos):
    x,y = pos
    return y//SQUARE_SIZE,x//SQUARE_SIZE



class Game:
    def __init__(self,WINDOW):
        
        self.window = WINDOW
        self.turn = WHITE
        self.moves = {}
        self.selected_piece = None
        self.locked_piece = None

        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
        self.progression = 0

        self.board = Board()


    def update(self):
        self.board.draw(self.window)
    
    def get_selected_piece(self,row,col):
        if self.board.board[row][col]:
            return self.board.board[row][col]
        
    def select_turn_piece(self,row,col):
        if self.board.board[row][col] and self.board.board[row][col].color == self.turn:
            return self.board.board[row][col]


    def swap_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE



    def show_moves(self,piece):
        moves = piece.get_move(self.board.board)
        piece.show_move(self.window,moves)
        return moves

    def show_capturing_moves(self,piece):
          return piece.show_capturing_moves(self.window,self.board.board)

    def make_move(self,moves,piece):
        row,col = get_row_col(pygame.mouse.get_pos())

        if (row,col) in moves:
            self.board.board[row][col] = piece
            self.board.board[piece.row][piece.col] = None
            self.progression += 1
            piece.row,piece.col = row,col

            piece.check_if_king(piece.row)
            self.swap_turn()
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
            self.progression = 0
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
    
    def check_win(self):
        if self.black_left <= 0:
            self.display_TEXT("WHITE is Winner !!!")
            return True
        elif self.white_left <= 0:
            self.display_TEXT("BLACK is Winner !!!")
            return True
        else:
            return False
        

    def check_no_legal_moves(self):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.board[row][col] != None:
                    piece = self.board.board[row][col]
                    if piece.color == self.turn:
                        move = piece.get_move(self.board.board)
                        if move:
                            legal_moves.append(move)
                        
                        captures = piece.get_capture_moves(self.board.board)
                        if captures:
                            legal_moves.append(captures)


        if legal_moves:return False      
        else:
            color = "WHITE" if WHITE != self.turn else "BLACK"
            self.display_TEXT(color + " is Winner") 
            return True

    def check_tie(self):
        if self.progression >= 50:
            self.display_TEXT("It's a Tie")
            return True
        return False

    def display_TEXT(self,winner_text):
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render(winner_text, True, (255, 255, 255))
        self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        
    
