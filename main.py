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

scroll = [0,0]
moveleft = False
moveright = False
jump = False

prev_time = time.time()
dt = 0

getTicksLastFrame = 0
Running = True
CanJump = False
applyGravity = True

player = Player()
#objects
objects = [Object(50-scroll[0],700,50,50, (0,0,0)), Object(500, 750, 50, 50, (255,255,255)), Object(475, 700, 100, 50, (255,0,0))]
while Running:
    clock.tick(300)
    now = time.time()
    dt = now - prev_time
    prev_time = now
    screen.fill((146,244,255))


    scroll[0] += (player.position.x-scroll[0] - WINDOW_SIZE[0]/2)/200
    scroll[1] += (player.position.y-scroll[1] - WINDOW_SIZE[1]/2)/200
    if scroll[1] > 0:
        scroll[1] = 0

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




    collision_tolerance = 5
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
            elif abs(object_bottom - player.position.y) < collision_tolerance:
                if player.y_momentum < 0:
                    player.y_momentum = 0
                applyGravity = True
            elif abs(object_right - player.position.x) < collision_tolerance:
                if (xbefore - player.position.x) > 0:
                    player.position.x = object_right
            elif abs(object.x - player_right) < collision_tolerance:
                if (xbefore - player.position.x) < 0:
                    player.position.x = object.x - 50
            
        object.draw(screen, scroll[0], scroll[1])


    if CanJump == True and jump == True:
        player.y_momentum = -500
        CanJump = False

    if applyGravity == True:
        player.y_momentum += player.gravity * dt
        CanJump = False


    player.position.y += player.y_momentum * dt
    Player.Draw(screen, player.position.x - scroll[0], player.position.y - scroll[1])
    pygame.display.update()
    applyGravity = True
    xbefore = player.position.x
pygame.quit()