# -*- coding: utf-8 -*-

import pygame, sys
from worm import *
from pygame.locals import *
from random import randrange

pygame.init()
clock = pygame.time.Clock()

WIDTH = 640
HEIGHT = 480

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Worm")

# Resources
BASICFONT = pygame.font.Font("freesansbold.ttf", 16)
appleSound = pygame.mixer.Sound("resources/sounds/apple.wav")

worm = Worm()

pos = [0,0]

gameover = worm.add(pos)

vel = (1, 0)
apple = (randrange(1, WIDTH/16), randrange(1, HEIGHT/16)) 

velLeft = {(1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1), (0,1):(1,0)}
velRight = {(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}

while not gameover:
    window.fill((0,0,0))
    # Updating worm
    pos[0] += vel[0]
    pos[1] += vel[1]
    if pos[0] >= WIDTH/16:
        pos[0] = 0
    elif pos[0] < 0:
        pos[0] = WIDTH/16 - 1
    if pos[1] >= HEIGHT/16:
        pos[1] = 0
    elif pos[1] < 0:
        pos[1] = HEIGHT/16 - 1
    gameover = worm.add(tuple(pos))

    # Logic with apple
    if apple[0] == pos[0] and apple[1] == pos[1]:
        worm.eatApple()
        appleSound.play()
        while apple in worm.structure:
            apple = (randrange(0, WIDTH/16), randrange(0, HEIGHT/16))

    # Rendering score
    score = BASICFONT.render("Score: {0}".format(worm.score), True, (255, 255, 255))
    scoreRectangle = score.get_rect().topleft = (WIDTH - 110, 10)
    window.blit(score, scoreRectangle)
    # Rendering worm
    for piece in worm.structure:
        x = piece[0]
        y = piece[1]
        pygame.draw.rect(window, (255, 255, 255), (x*16, y*16, 16, 16))

    # Rendering apple
    pygame.draw.rect(window, (200, 0, 0), (apple[0]*16, apple[1]*16, 16, 16))

    # Processing input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                vel = velRight[vel]
            elif event.key == K_LEFT:
                vel = velLeft[vel]
                

    pygame.display.update()
    clock.tick(8)

if gameover:
    pygame.quit()
    print "Your score is: ", worm.score, "\n"
