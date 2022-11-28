import pygame, math

class Gun:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
        self.image = pygame.image.load("imgs/Pistol1.png").convert_alpha()
        self.rot_image = self.image.copy()
        self.angle = self.rotate(pygame.mouse.get_pos())
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.rot_image, (self.x - scroll_x, self.y - scroll_y))
    def rotate(self, mouse):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        offset = (mouse[1]-self.rect.centery, mouse[0]-self.rect.centerx)
        self.angle = 360-math.degrees(math.atan2(*offset))
        self.rot_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)