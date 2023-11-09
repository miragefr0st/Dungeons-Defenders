import pygame
import sys
import start
from assets import *


def howtoplay():
    backround = pygame.image.load("res/how-to-play.gif")
    while True:
        screen.blit(backround, [0, 0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_SPACE]:
            start.start()
        pygame.display.flip()