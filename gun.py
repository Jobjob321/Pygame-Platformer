import pygame, math

class Gun:
    def __init__(self, player_x, player_y,mouse_x, mouse_y):
        self.x = player_x
        self.y = player_y
        self.image = pygame.image.load("imgs/Pistol1.png").convert_alpha()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.image, angle)

    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.x - scroll_x, self.y - scroll_y))