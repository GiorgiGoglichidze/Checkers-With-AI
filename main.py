import pygame
from Checkers.constants import HEIGHT,WIDTH,WHITE,BLACK,SQUARE_SIZE 
from Checkers.board import Board
from Checkers.game import Game
from minimax.algorithm import minimax
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

        if game.board.turn == BLACK:
            min_val,new_board = minimax(game.board,5,False)
            game.ai_move(new_board)
            game.update()
            pygame.time.delay(500)


        for event in pygame.event.get():
            tie = game.display_tie()
            if tie:
                run = False
                break

            if game.display_no_legal_moves():
                    run = False
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                square = get_row_col(pygame.mouse.get_pos())
                game.handle_click(square)

            winner = game.display_win()
            if winner:
                run = False
                break

            if event.type == pygame.QUIT:
                run = False
                break


        pygame.display.flip()

if "__main__" == __name__:
    main()