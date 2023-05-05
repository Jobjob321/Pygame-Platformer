import pygame

class Gun:
    def __init__(self,):
        self.image = pygame.image.load("imgs/Pistol1.png").convert_alpha()
        self.Rotated = False
    def draw(self, screen, scroll_x, scroll_y,player_x, player_y, Moveleft, Moveright):
        self.x = player_x
        self.y = player_y

        if Moveleft == True and self.Rotated == False:
            self.Rotated = True
            self.image = pygame.transform.flip(self.image, True, False)
        
        if Moveright == True and self.Rotated == True:
            self.Rotated = False
            self.image = pygame.transform.flip(self.image, True, False)

        
        if self.Rotated == True:
            self.x -= 20
        if self.Rotated == False:
            self.x += 20


        screen.blit(self.image, (self.x - scroll_x, self.y - scroll_y))