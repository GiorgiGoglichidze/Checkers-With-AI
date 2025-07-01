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
    #game.turn = WHITE
    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if capture_moves and event.type == pygame.MOUSEBUTTONDOWN:
                game.capture_piece(capture_moves,piece)
                game.update()


                capture_moves = piece.show_capture_moves(WINDOW, game.board.board)

                if not capture_moves:
                    piece = None
                    swap_turn(game)


            elif moves and event.type == pygame.MOUSEBUTTONDOWN:
                game.make_move(moves,piece)
                game.update()
                piece = None
                moves = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.update()
                row,col = get_row_col(pygame.mouse.get_pos())
                piece = game.get_selected_piece(row,col)
                if piece and piece.color == game.turn:
                    moves = game.show_moves(piece)
                    capture_moves = piece.show_capture_moves(WINDOW,game.board.board)


            if event.type == pygame.QUIT:
                run = False
                break


        pygame.display.flip()

if "__main__" == __name__:
    main()