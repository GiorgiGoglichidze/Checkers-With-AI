import pygame
from Checkers.constants import HEIGHT,WIDTH,WHITE,SQUARE_SIZE 
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

def main():
    run = True
    game = Game(WINDOW)
    game.update()
    piece = None
    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if piece and event.type == pygame.MOUSEBUTTONDOWN:
                game.make_move(moves,piece)
                game.update()
                piece = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.update()
                row,col = get_row_col(pygame.mouse.get_pos())
                piece = game.get_selected_piece(row,col)
                if piece:
                    moves = game.show_moves(piece)

            if event.type == pygame.QUIT:
                run = False
                break


        pygame.display.flip()

if "__main__" == __name__:
    main()