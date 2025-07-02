import pygame
#SIZE Parameteres
WIDTH,HEIGHT = 800,800
ROWS,COLS = 8,8
SQUARE_SIZE = WIDTH // COLS
RADIUS_PIECE = 30
RADIUS_MOVE = 10
#Colors

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

#Assets
CROWN = pygame.transform.scale(pygame.image.load('Assets/crown.png'),(40,25))

