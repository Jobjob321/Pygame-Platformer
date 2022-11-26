import pygame

class Object:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,self.color, self.rect)