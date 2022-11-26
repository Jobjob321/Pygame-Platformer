import pygame
from Player import Player
from object import Object
from utils import checkCollisions
from pygame.locals import *
pygame.init()

WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]), 0 ,32)



moveleft = False
moveright = False
jump = False



getTicksLastFrame = 0
Running = True
CanJump = False
applyGravity = True

#objects
player = Player()
objects = [Object(50,700,50,50), Object(500, 700, 75, 100)]
while Running:
    fps = pygame.time.get_ticks()
    dt = (fps - getTicksLastFrame) / 1000
    getTicksLastFrame = fps
    screen.fill((146,244,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                moveleft = True
            if event.key == K_d or event.key == K_RIGHT:
                moveright = True
            if event.key == K_SPACE:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                moveleft = False
            if event.key == K_d or event.key == K_RIGHT:
                moveright = False
            if event.key == K_SPACE:
                jump = False

    
    if moveleft == True:
        player.position.x -= 200 * dt
    if moveright == True:
        player.position.x += 200 * dt
    
    if player.position.y + 50 > WINDOW_SIZE[1] and player.y_momentum > 0:
        player.y_momentum = 0
        CanJump = True

    

    
    collision_tolerance = 2
    for object in objects:
        if checkCollisions(object.x, object.y, object.width, object.height, player.position.x, player.position.y, 50, 50):
            player_bottom = player.position.y  + 50
            player_right = player.position.x + 50
            object_bottom = object.y + object.height
            object_right = object.x + object.width
            if abs(object.y - player_bottom) < collision_tolerance:
                if player.y_momentum >= 0:
                    applyGravity = False
                    player.y_momentum = 0
                    CanJump = True
            if abs(object_bottom - player.position.y) < collision_tolerance:
                if player.y_momentum < 0:
                    player.y_momentum = 0
                applyGravity = True
            if abs(object_right - player.position.x) < collision_tolerance:
                player.position.x = object_right
            if abs(object.x - player_right) < collision_tolerance:
                player.position.x = object.x - 50

        else:
            applyGravity = True
        object.draw(screen)

    if applyGravity == True:
        player.y_momentum += player.gravity * dt
    
    if CanJump == True and jump == True:
        player.y_momentum -= 250 * dt
        CanJump = False


    player.position.y += player.y_momentum
    Player.Draw(screen, player.position.x, player.position.y)
    pygame.display.update()

pygame.quit()