import pygame
from Checkers.constants import HEIGHT,WIDTH,WHITE,SQUARE_SIZE 
from Checkers.board import Board

pygame.init()

FPS = 60
clock = pygame.time.Clock()


WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")





def main():
    run = True
    board = Board()
    board.draw(WINDOW)
    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                board.draw(WINDOW)
                pos = pygame.mouse.get_pos()
                x,y = pos
                row,col = y//SQUARE_SIZE,x//SQUARE_SIZE
                board.show_moves(WINDOW,col,row)

        pygame.display.flip()

if "__main__" == __name__:
    main()