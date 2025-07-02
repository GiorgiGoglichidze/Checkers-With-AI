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



def main():
    run = True
    game = Game(WINDOW)
    game.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            tie = game.check_tie()
            if tie:
                run = False
                break

            if game.check_no_legal_moves():
                    run = False
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                square = get_row_col(pygame.mouse.get_pos())
                game.handle_click(square)

            winner = game.check_win()
            if winner:
                run = False
                break

            if event.type == pygame.QUIT:
                run = False
                break


        pygame.display.flip()

if "__main__" == __name__:
    main()