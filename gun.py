import pygame

class Gun:
    def __init__(self,):
        self.image = pygame.image.load("imgs/Pistol1.png").convert_alpha()
        self.rotleft = False
        self.rotright = False
        self.rot: int = 0
    def draw(self, screen, scroll_x, scroll_y,player_x, player_y):
        self.x = player_x
        self.y = player_y
        if self.rot <= -360 or self.rot >= 360:
                self.rot = 0
        if self.rotleft == True:
            self.rot += 3
        elif self.rotright == True:
            self.rot -= 3
        self.image = pygame.transform.rotozoom(self.image, self.rot, 1)
        screen.blit(self.image, (self.x - scroll_x, self.y - scroll_y))