import pygame

class Gun:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
        self.image = pygame.image.load("imgs/Pistol1.png").convert_alpha()
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.x - scroll_x, self.y - scroll_y))