import pygame
from Player import Player
from object import Object
from utils import checkCollisions
from pygame.locals import *
import time
pygame.init()

WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]), 0 ,32)
clock = pygame.time.Clock()


moveleft = False
moveright = False
jump = False

prev_time = time.time()
dt = 0

getTicksLastFrame = 0
Running = True
CanJump = False
applyGravity = True

#objects
player = Player()
objects = [Object(50,700,50,50), Object(500, 700, 75, 100)]
while Running:
    clock.tick(300)
    now = time.time()
    dt = now - prev_time
    prev_time = now
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
    
    if player.position.y + 50 >= WINDOW_SIZE[1] and player.y_momentum > 0:
        player.y_momentum = 0
        player.position.y = WINDOW_SIZE[1] - 50
        CanJump = True
        applyGravity = False

    

    
    collision_tolerance = 10
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
            
        object.draw(screen)


    if CanJump == True and jump == True:
        player.y_momentum -= 500
        CanJump = False

    if applyGravity == True:
        player.y_momentum += player.gravity * dt
        CanJump = False


    player.position.y += player.y_momentum * dt
    Player.Draw(screen, player.position.x, player.position.y)
    pygame.display.update()
    applyGravity = True
pygame.quit()