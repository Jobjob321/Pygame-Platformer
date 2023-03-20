import pygame, time

class Bullet:
    def __init__(self, x, y, moveleft, image):
        self.x = x
        self.y = y
        self.velocity = 1
        self.velocity_y = 0

        self.moveleft = moveleft
        self.timer = time.time()
        self.image = image

        if self.moveleft == True:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velocity = -1
    def draw(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (self.x - scroll_x, self.y - scroll_y))

        