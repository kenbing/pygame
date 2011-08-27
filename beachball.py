import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])
my_ball = pygame.image.load('beach_ball.png')
x = 50 
y = 50
x_speed = 5
y_speed = 5

'''
screen.blit(my_ball, [x, y])
pygame.time.delay(2000)
pygame.display.flip()
pygame.time.delay(2000)
pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
x += 50
screen.blit(my_ball, [x, y])
pygame.display.flip()
pygame.time.delay(2000)
pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
x += 50
screen.blit(my_ball, [x, y])
pygame.display.flip()
pygame.time.delay(2000)
pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
x += 50
screen.blit(my_ball, [x, y])
pygame.display.flip()


screen.blit(my_ball, [x, y])
pygame.display.flip()
for looper in range(0, 10):
    pygame.time.delay(2000)
    pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
    x = x + x_speed
    global x
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

for looper in range(0, 10):
    pygame.time.delay(2000)
    pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
    x = x - x_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    pygame.time.delay(20)
    pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed

    if x > screen.get_width() - 90 or x < 0:
    #if x > 550 or x < 0:
        x_speed = - x_speed
    #if y > 390 or y < 0:
    if y > screen.get_height() - 90 or y < 0:
        y_speed = - y_speed
    '''

    x = x + x_speed
    if x > screen.get_width():
        x = -219
    '''
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

