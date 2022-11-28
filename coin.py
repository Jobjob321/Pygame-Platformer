import pygame

class Coin:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, screen, scroll_x, scroll_y, coin_image):
        screen.blit(coin_image, (self.x - scroll_x, self.y - scroll_y))