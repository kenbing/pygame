import pygame, sys
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])

pygame.time.delay5)
plot_points = []
for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plot_points.append([x, y])
pygame.draw.lines(screen, [255, 255, 255], False, plot_points, 1)
#pygame.draw.rect(screen, [255, 255, 255], [x, y, 1, 1], 1)
pygame.display.flip()
pygame.time.delay(5000)

'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
'''
