import pygame
from Checkers.constants import HEIGHT,WIDTH,WHITE,BLACK,SQUARE_SIZE 
from Checkers.board import Board
from Checkers.game import Game
pygame.init()

FPS = 60
clock = pygame.time.Clock()


WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col(pos):
    x,y = pos
    return y//SQUARE_SIZE,x//SQUARE_SIZE

def swap_turn(game):
    if game.turn == WHITE:
        game.turn = BLACK
    else:
        game.turn = WHITE

def main():
    run = True
    game = Game(WINDOW)
    game.update()
    piece = None
    capture_moves = None
    moves = None

    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if game.check_no_legal_moves():
                    run = False
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                


                square = get_row_col(pygame.mouse.get_pos())
                while capture_moves and piece and  square in capture_moves:
                    print('LEILA')
                    game.capture_piece(capture_moves,piece)
  
                    game.update()
                    capture_moves = piece.get_capture_moves(game.board.board)

                    if not capture_moves:
                        piece.check_if_king(piece.row)
                        piece = None
                        swap_turn(game)
                    capture_moves = None


                if moves and square in moves and piece:
                    print('SONIAAAAAA')
                    game.make_move(moves,piece)
                    game.update()
                    piece = None
                    moves = None

                else:                
                    game.update()
                    piece = game.select_turn_piece(square[0],square[1])                  
                    if piece and piece.color == game.turn:
                        print('ZAURAAAA')
                        capturing_pieces = game.get_all_capturing_pieces()
                        if capturing_pieces:
                            print('MURTAZIIII')
                            capture_moves = piece.get_capture_moves(game.board.board)
                            if capture_moves:
                                piece.show_capture_moves(game.window,capture_moves)
                                moves = None
                        else:
                            
                            moves = game.show_moves(piece)

                    winner = game.check_win()
                    tie = game.check_tie()
                    if winner or tie:
                        run = False
                        break

            if event.type == pygame.QUIT:
                run = False
                break


        pygame.display.flip()

if "__main__" == __name__:
    main()