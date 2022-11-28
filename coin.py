import pygame

class Coin:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def draw(self, screen, scroll_x, scroll_y):
        coin = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.width, self.height)
        pygame.draw.rect(screen, (0,255,0), coin)