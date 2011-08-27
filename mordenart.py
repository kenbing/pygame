#!/usr/bin/python2
# coding:utf-8

import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])

#pygame.draw.circle(screen, [255, 0, 0], [320, 240], 30, 0)
#pygame.draw.rect(screen, [255, 0, 0], [250, 150, 300, 200], 10)

for i in range(100):
    width = random.randint(0, 200)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, color, [left, top, width, height], 3)
    pygame.time.delay(30)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
