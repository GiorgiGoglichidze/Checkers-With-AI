from .constants import ROWS,COLS,SQUARE_SIZE,WHITE,GREEN,BLACK,WIDTH,HEIGHT
import pygame
class Board:
    def __init__(self):
        self.board = []
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
        self.progression = 0
        self.turn = WHITE

        self.create_board()

    def king_count(self,color):

        if color == WHITE:
            self.white_kings+=1
        else:
            self.black_kings+=1
    
    def set_white_left(self,white_left):
        self.white_left = white_left
    
    def set_black_left(self,black_left):
        self.black_left = black_left

    def set_progression(self,progression):
        self.progression = progression
    
    def set_turn(self,turn):
        self.turn = turn

    def swap_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE


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


    def evaluate_board(self):
        white_score = 0
        black_score = 0

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece:
                    value = 1
                    if piece.king:
                        value = 2  # Give kings higher value

                    # Positional bonus: center columns
                    if 2 <= col <= 5:
                        value += 0.2

                    # Progress bonus: closer to promotion
                    if piece.color == WHITE:
                        value += (7 - row) * 0.05
                        white_score += value
                    else:
                        value += row * 0.05
                        black_score += value

        return white_score - black_score
            
    def draw_pieces(self,WINDOW):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is not None:
                    self.board[row][col].draw(WINDOW)

    def draw(self,WINDOW):
        self.draw_squares(WINDOW)
        self.draw_pieces(WINDOW)

    def check_win(self):
        if self.black_left <= 0:
            return 1
        elif self.white_left <= 0:
            return 2
        else:
            return False
        

    def check_no_legal_moves(self):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    if piece.color == self.turn:
                        move = piece.get_moves(self.board)
                        if move:
                            legal_moves.append(move)
                        
                        captures = piece.get_capture_moves(self.board)
                        if captures:
                            legal_moves.append(captures)


        if legal_moves:return False      
        else:
            return True

    def check_tie(self):
        if self.progression >= 50:
            return True
        return False

    def game_over(self):
        if self.check_tie() or self.check_no_legal_moves() or  self.check_win():
            return True
        else:
            return False


