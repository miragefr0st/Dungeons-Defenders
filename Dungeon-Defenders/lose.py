import pygame
import sys
from assets import *
import game


def lose(wave):
    backround = pygame.image.load("res/start.gif")
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
            game.game()
        renderedText = font5.render("Vous avez survece a: " + str(wave) + " Vagues", 1, red, )
        screen.blit(renderedText, (125, 50))
        renderedText = font4.render("Appuyer sur ESPACE pour rejouer", 1, red)
        screen.blit(renderedText, (19, 350))
        pygame.display.flip()        