import pygame
from pygame.locals import *

class Player:
    position = pygame.Vector2(200,500)
    y_momentum = 0.0
    gravity = 1000.0
    def Draw(screen, x, y):
        player_rect = pygame.Rect(x, y,50,50)
        pygame.draw.rect(screen, (0,0,0), player_rect)