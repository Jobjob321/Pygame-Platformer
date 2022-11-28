import pygame, math
from Player import Player
from object import Object
from utils import checkCollisions
from gun import Gun
from coin import Coin
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
mouse = [0,0]

prev_time = time.time()
dt = 0

getTicksLastFrame = 0
Running = True
CanJump = False
applyGravity = True


FONT = pygame.font.SysFont("Helvetica-bold", 50)

player = Player()
#objects
objects = [
    Object(50,700,50,50, (0,0,0)),
    Object(500, 750, 50, 50, (255,255,255)),
    Object(475, 700, 100, 50, (255,0,0)),
    Object(1000,700,50,100, (255,255,255))
]

coins = [Coin(700, 550), Coin(900, 700)]
coinimage = pygame.image.load("imgs/Coin.png").convert_alpha()
coinamount = 0
while Running:
    clock.tick(144)
    now = time.time()
    dt = now - prev_time
    prev_time = now
    screen.fill((146,244,255))

    mouse = pygame.mouse.get_pos()
    scroll[0] += (player.position.x-scroll[0] - WINDOW_SIZE[0]/2) * 2.5 * dt
    scroll[1] += (player.position.y-scroll[1] - WINDOW_SIZE[1]/2) * 2.5 * dt
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
    
    if player.position.y + 50 >= WINDOW_SIZE[1] and player.y_momentum > 0:
        player.y_momentum = 0
        player.position.y = WINDOW_SIZE[1] - 50
        CanJump = True
        applyGravity = False

    collision_tolerance = 3
    for i in range(10):
        pistol = Gun(player.position.x, player.position.y, mouse[0],mouse[1])
        if moveleft == True:
            player.position.x -= 25 * dt
        if moveright == True:
            player.position.x += 25 * dt
        if CanJump == True and jump == True:
            player.y_momentum = -70
            CanJump = False
        if applyGravity == True:
            player.y_momentum += player.gravity * dt
            CanJump = False
        player.position.y += player.y_momentum * dt
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
                    player.position.y = object_bottom
                    if player.y_momentum <= 0:
                        player.y_momentum = 0
                    applyGravity = True
                elif abs(object_right - player.position.x) < collision_tolerance:
                    if (xbefore - player.position.x) > 0:
                        player.position.x = object_right
                elif abs(object.x - player_right) < collision_tolerance:
                    if (xbefore - player.position.x) < 0:
                        player.position.x = object.x - 50
            object.draw(screen, scroll[0], scroll[1])
        
        for coin in coins:
            if checkCollisions(coin.x, coin.y, coin.width, coin.height, player.position.x, player.position.y, 50, 50):
                coinamount += 1
                print(coinamount)
                coins.remove(coin)
            coin.draw(screen, scroll[0], scroll[1], coinimage)




    cointext = FONT.render("Coins: " + str(coinamount), 1, (0,0,0))
    screen.blit(cointext, (10, 10))

    Player.Draw(screen, player.position.x - scroll[0], player.position.y - scroll[1])
    pistol.draw(screen, scroll[0], scroll[1])

    pygame.display.update()
    applyGravity = True
    xbefore = player.position.x
pygame.quit()